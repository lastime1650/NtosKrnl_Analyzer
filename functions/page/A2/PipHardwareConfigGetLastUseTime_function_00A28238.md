# PipHardwareConfigGetLastUseTime

- RVA: `0x00A28238`–`0x00A282C4` (길이 `140` bytes)
- VA: `0x0000000140A28238`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC048`
- 디코드: `37`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A2826A` → [PipHardwareConfigOpenKey](../AD/PipHardwareConfigOpenKey_function_00AD8848.md) (function, `0x00AD8848`)
- `0x00A2829D` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x00A282B1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- [PnpGetStableSystemBootTime](PnpGetStableSystemBootTime_function_00A27C10.md) at `0x00A27C3D`

### Static image references
- `0x00A28289` → RVA `0x00AFD420` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A282B1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A28238  48 8B C4                        mov rax, rsp
00A2823B  48 89 58 20                     mov qword ptr [rax + 0x20], rbx
00A2823F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00A28243  56                              push rsi
00A28244  48 83 EC 30                     sub rsp, 0x30
00A28248  83 60 10 00                     and dword ptr [rax + 0x10], 0
00A2824C  48 8B F2                        mov rsi, rdx
00A2824F  48 83 60 18 00                  and qword ptr [rax + 0x18], 0
00A28254  48 85 D2                        test rdx, rdx
00A28257  75 07                           jne 0x140a28260
00A28259  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00A2825E  EB 56                           jmp 0x140a282b6
00A28260  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00A28265  BA 19 00 02 00                  mov edx, 0x20019
00A2826A  E8 D9 05 0B 00                  call 0x140ad8848
00A2826F  8B D8                           mov ebx, eax
00A28271  85 C0                           test eax, eax
00A28273  78 2F                           js 0x140a282a4
00A28275  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00A2827A  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00A2827F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A28284  4C 8D 4C 24 48                  lea r9, [rsp + 0x48]
00A28289  4C 8D 05 90 51 0D 00            lea r8, [rip + 0xd5190]
00A28290  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A28295  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
00A2829D  E8 5A BE F6 FF                  call 0x1409940fc
00A282A2  8B D8                           mov ebx, eax
00A282A4  48 83 7C 24 50 00               cmp qword ptr [rsp + 0x50], 0
00A282AA  74 0A                           je 0x140a282b6
00A282AC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00A282B1  E8 FA 4F C8 FF                  call 0x1406ad2b0
00A282B6  8B C3                           mov eax, ebx
00A282B8  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00A282BD  48 83 C4 30                     add rsp, 0x30
00A282C1  5E                              pop rsi
00A282C2  C3                              ret
00A282C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipHardwareConfigGetLastUseTime(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 32) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (48);
    if (a2 != 0) goto loc_00A28260;
    goto loc_00A282B6;
loc_00A28260:
    result = PipHardwareConfigOpenKey(a1, (unsigned int)(0x20019ULL), v_stack_p18, a4);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = v_stack_p18;
        result = v_stack_p8;
        v_stack_m10 = result;
        a4 = v_stack_p10;
        a3 = v_rip + 872848;
        v_stack_m18 = a2;
        v_stack_p8 = 8;
        result = PnpCtxRegQueryValue(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (v_stack_p18 != 0) {
        a1 = v_stack_p18;
        result = ZwClose(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t PipHardwareConfigGetLastUseTime(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x20) = local_rbx;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (48);
    if (Arg2 != 0) goto loc_00A28260;
    goto loc_00A282B6;
loc_00A28260:
    result = PipHardwareConfigOpenKey(Arg1, (uint32_t)(0x20019ULL), v_stack_p18, a4);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = v_stack_p18;
        result = v_stack_p8;
        v_stack_m10 = result;
        a4 = v_stack_p10;
        a3 = v_rip + 872848;
        v_stack_m18 = Arg2;
        v_stack_p8 = 8;
        result = PnpCtxRegQueryValue(Arg1, Arg2, a3, a4);
        local_rbx = (uint32_t)(result);
    }
    if (v_stack_p18 != 0) {
        Arg1 = v_stack_p18;
        result = ZwClose(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A28238&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A28238[BB_00A28238]
  bb_00A28259[BB_00A28259]
  bb_00A28260[BB_00A28260]
  bb_00A28275[BB_00A28275]
  bb_00A282A4[BB_00A282A4]
  bb_00A282AC[BB_00A282AC]
  bb_00A282B6[BB_00A282B6]
  bb_00A282C3[BB_00A282C3]
  bb_00A28238 -->|branch| bb_00A28260
  bb_00A28238 -->|fallthrough| bb_00A28259
  bb_00A28259 -->|branch| bb_00A282B6
  bb_00A28260 -->|branch| bb_00A282A4
  bb_00A28260 -->|fallthrough| bb_00A28275
  bb_00A28275 -->|flow| bb_00A282A4
  bb_00A282A4 -->|branch| bb_00A282B6
  bb_00A282A4 -->|fallthrough| bb_00A282AC
  bb_00A282AC -->|flow| bb_00A282B6
```
