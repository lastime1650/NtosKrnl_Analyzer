# MiReleasePrivilegedPtes

- RVA: `0x007F9264`–`0x007F92DA` (길이 `118` bytes)
- VA: `0x00000001407F9264`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `32`개 명령, `118/118` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007F92A8` → [KeReservePrivilegedPages](../../text/4B/KeReservePrivilegedPages_function_004BEAE8.md) (function, `0x004BEAE8`)
- `0x007F92C8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [MiGetSystemAddressForImage](../A7/MiGetSystemAddressForImage_function_00A74EEC.md) at `0x00A750A4`
- [MiUnloadSystemImage](../AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA33B9`

### Static image references
- `0x007F926E` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007F92A8` → [KeReservePrivilegedPages](../../text/4B/KeReservePrivilegedPages_function_004BEAE8.md) (`PAGE` → `.text`)
  - `0x007F92C8` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F9264  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007F9269  57                              push rdi
007F926A  48 83 EC 30                     sub rsp, 0x30
007F926E  48 F7 05 0F D8 7C 00 00 40 00 00  test qword ptr [rip + 0x7cd80f], 0x4000
007F9279  48 8B DA                        mov rbx, rdx
007F927C  48 8B F9                        mov rdi, rcx
007F927F  74 4D                           je 0x1407f92ce
007F9281  48 8B D1                        mov rdx, rcx
007F9284  48 C1 E2 19                     shl rdx, 0x19
007F9288  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
007F9292  48 C1 E0 19                     shl rax, 0x19
007F9296  41 B9 01 00 00 00               mov r9d, 1
007F929C  48 2B D0                        sub rdx, rax
007F929F  44 8B C3                        mov r8d, ebx
007F92A2  48 C1 FA 10                     sar rdx, 0x10
007F92A6  33 C9                           xor ecx, ecx
007F92A8  E8 3B 58 CC FF                  call 0x1404beae8
007F92AD  85 C0                           test eax, eax
007F92AF  79 1D                           jns 0x1407f92ce
007F92B1  48 98                           cdqe
007F92B3  4C 8B CB                        mov r9, rbx
007F92B6  4C 8B C7                        mov r8, rdi
007F92B9  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007F92BE  BA 16 15 05 00                  mov edx, 0x51516
007F92C3  B9 1A 00 00 00                  mov ecx, 0x1a
007F92C8  E8 93 43 D0 FF                  call 0x1404fd660
007F92CD  CC                              int3
007F92CE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
007F92D3  48 83 C4 30                     add rsp, 0x30
007F92D7  5F                              pop rdi
007F92D8  C3                              ret
007F92D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleasePrivilegedPtes(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    if (((*(unsigned __int64 *)(v_rip + 8181775)) & (0x4000ULL)) == 0) goto loc_007F92CE;
    a2 = (a1) << (25);
    result = (result) << (25);
    a2 = (a2) - (result);
    a2 = (a2) >> (16);
    a1 = 0;
    result = KeReservePrivilegedPages(a1, a2, (unsigned int)((unsigned int)(a2)), 1);
    if (sign_flag) {
        a4 = a2;
        a3 = 0;
        v_stack_m18 = result;
        a2 = 0x51516ULL;
        a1 = 26;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleasePrivilegedPtes(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    if (((*(uint64_t *)(v_rip + 0x7CD80F)) & (0x4000ULL)) == 0) goto loc_007F92CE;
    Arg2 = (Arg1) << (25);
    result = (result) << (25);
    Arg2 = (Arg2) - (result);
    Arg2 = (Arg2) >> (16);
    Arg1 = 0;
    result = KeReservePrivilegedPages(Arg1, Arg2, (uint32_t)((uint32_t)(Arg2)), 1);
    if (sign_flag) {
        a4 = Arg2;
        a3 = 0;
        v_stack_m18 = result;
        Arg2 = 0x51516ULL;
        Arg1 = 26;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F9264&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F9264[BB_007F9264]
  bb_007F9281[BB_007F9281]
  bb_007F92B1[BB_007F92B1]
  bb_007F92CE[BB_007F92CE]
  bb_007F92D9[BB_007F92D9]
  bb_007F9264 -->|branch| bb_007F92CE
  bb_007F9264 -->|fallthrough| bb_007F9281
  bb_007F9281 -->|branch| bb_007F92CE
  bb_007F9281 -->|fallthrough| bb_007F92B1
  bb_007F92B1 -->|flow| bb_007F92CE
```
