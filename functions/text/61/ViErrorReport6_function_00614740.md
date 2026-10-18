# ViErrorReport6

- RVA: `0x00614740`–`0x006147CB` (길이 `139` bytes)
- VA: `0x0000000140614740`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A9C4`
- 디코드: `39`개 명령, `139/139` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00614769` → [ViErrorDisplayDescription](../../pagevrfy/BA/ViErrorDisplayDescription_function_00BA361C.md) (function, `0x00BA361C`)
- `0x0061478B` → [RtlStringCbPrintfA](../53/RtlStringCbPrintfA_function_0053BC0C.md) (function, `0x0053BC0C`)
- `0x00614799` → [VfUtilDbgPrint](VfUtilDbgPrint_function_006122AC.md) (function, `0x006122AC`)
- `0x006147A9` → [ViErrorFinishReport](../../pagevrfy/BA/ViErrorFinishReport_function_00BA366C.md) (function, `0x00BA366C`)
- `0x006147B9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ViGenericVerifyIrpStackDownward](../../pagevrfy/B9/ViGenericVerifyIrpStackDownward_function_00B93F90.md) at `0x00B94158`
- [ViGenericVerifyIrpStackUpward](../../pagevrfy/B9/ViGenericVerifyIrpStackUpward_function_00B94190.md) at `0x00B9422E`
- [IovpCallDriver2](../../pagevrfy/B9/IovpCallDriver2_function_00B9D270.md) at `0x00B9D3F4`
- [IovpCallDriver2](../../pagevrfy/B9/IovpCallDriver2_function_00B9D270.md) at `0x00B9D44C`
- [sub_00BBBE00](../../pagevrfy/BB/Unknown_function_00BBBE00.md) at `0x00BBBEE2`

### Static image references
- `0x0061474C` → RVA `0x00E0A740` (`.data`; read)
- `0x00614775` → RVA `0x006CE6E0` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00614769` → [ViErrorDisplayDescription](../../pagevrfy/BA/ViErrorDisplayDescription_function_00BA361C.md) (`.text` → `PAGEVRFY`)
  - `0x006147A9` → [ViErrorFinishReport](../../pagevrfy/BA/ViErrorFinishReport_function_00BA366C.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00614740  40 53                           push rbx
00614742  55                              push rbp
00614743  56                              push rsi
00614744  57                              push rdi
00614745  48 81 EC A8 00 00 00            sub rsp, 0xa8
0061474C  48 8B 05 ED 5F 7F 00            mov rax, qword ptr [rip + 0x7f5fed]
00614753  48 33 C4                        xor rax, rsp
00614756  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
0061475E  49 63 E9                        movsxd rbp, r9d
00614761  49 8B F0                        mov rsi, r8
00614764  48 8B FA                        mov rdi, rdx
00614767  8B D9                           mov ebx, ecx
00614769  E8 AE EE 58 00                  call 0x140ba361c
0061476E  4C 8B CF                        mov r9, rdi
00614771  89 6C 24 28                     mov dword ptr [rsp + 0x28], ebp
00614775  4C 8D 05 64 9F 0B 00            lea r8, [rip + 0xb9f64]
0061477C  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00614781  BA 57 00 00 00                  mov edx, 0x57
00614786  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0061478B  E8 7C 74 F2 FF                  call 0x14053bc0c
00614790  85 C0                           test eax, eax
00614792  78 0A                           js 0x14061479e
00614794  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00614799  E8 0E DB FF FF                  call 0x1406122ac
0061479E  4C 8B CD                        mov r9, rbp
006147A1  4C 8B C6                        mov r8, rsi
006147A4  48 8B D7                        mov rdx, rdi
006147A7  8B CB                           mov ecx, ebx
006147A9  E8 BE EE 58 00                  call 0x140ba366c
006147AE  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
006147B6  48 33 CC                        xor rcx, rsp
006147B9  E8 82 7E 09 00                  call 0x1406ac640
006147BE  48 81 C4 A8 00 00 00            add rsp, 0xa8
006147C5  5F                              pop rdi
006147C6  5E                              pop rsi
006147C7  5D                              pop rbp
006147C8  5B                              pop rbx
006147C9  C3                              ret
006147CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViErrorReport6(int a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned __int64 v_stack_mA8;

    v_rsp = (v_rsp) - (168);
    result = (*(unsigned __int64 *)(v_rip + 8347629)) ^ (v_rsp);
    v_stack_m38 = result;
    result = ViErrorDisplayDescription(a1, a2, a3, a4);
    v_stack_mA0 = (unsigned int)((int)(a4));
    v_stack_mA8 = a3;
    result = RtlStringCbPrintfA(v_stack_m98, 87, v_rip + 761700, a2);
    if (!(sign_flag)) {
        a1 = v_stack_m98;
        result = VfUtilDbgPrint(a1, 87, v_rip + 761700, a2);
    }
    result = ViErrorFinishReport((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, (int)(a4));
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, (int)(a4));
    v_rsp = (v_rsp) + (168);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViErrorReport6(int32_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint64_t v_stack_mA8;

    local_rsp = (local_rsp) - (168);
    result = (*(uint64_t *)(v_rip + 0x7F5FED)) ^ (local_rsp);
    v_stack_m38 = result;
    result = ViErrorDisplayDescription(Arg1, Arg2, Arg3, Arg4);
    v_stack_mA0 = (uint32_t)((int32_t)(Arg4));
    v_stack_mA8 = Arg3;
    result = RtlStringCbPrintfA(v_stack_m98, 87, v_rip + 761700, Arg2);
    if (!(sign_flag)) {
        Arg1 = v_stack_m98;
        result = VfUtilDbgPrint(Arg1, 87, v_rip + 761700, Arg2);
    }
    result = ViErrorFinishReport((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, (int32_t)(Arg4));
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, (int32_t)(Arg4));
    local_rsp = (local_rsp) + (168);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00614740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00614740[BB_00614740]
  bb_00614794[BB_00614794]
  bb_0061479E[BB_0061479E]
  bb_006147CA[BB_006147CA]
  bb_00614740 -->|branch| bb_0061479E
  bb_00614740 -->|fallthrough| bb_00614794
  bb_00614794 -->|flow| bb_0061479E
```
