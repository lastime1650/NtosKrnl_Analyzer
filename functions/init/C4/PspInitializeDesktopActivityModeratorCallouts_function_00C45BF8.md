# PspInitializeDesktopActivityModeratorCallouts

- RVA: `0x00C45BF8`–`0x00C45C59` (길이 `97` bytes)
- VA: `0x0000000140C45BF8`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EAB4`
- 디코드: `24`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00C45C3D` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)

### Direct callers
- [PspInitPhase1](PspInitPhase1_function_00C453B8.md) at `0x00C45404`

### Static image references
- `0x00C45C1F` → RVA `0x00FC7028` (`ALMOSTRO`; read)
- `0x00C45C46` → RVA `0x00FC7028` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C45C3D` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C45BF8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C45BFD  55                              push rbp
00C45BFE  48 8B EC                        mov rbp, rsp
00C45C01  48 83 EC 60                     sub rsp, 0x60
00C45C05  33 DB                           xor ebx, ebx
00C45C07  48 C7 45 D0 07 00 01 00         mov qword ptr [rbp - 0x30], 0x10007
00C45C0F  48 8D 45 C0                     lea rax, [rbp - 0x40]
00C45C13  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
00C45C17  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C45C1B  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C45C1F  48 8D 0D 02 14 38 00            lea rcx, [rip + 0x381402]
00C45C26  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
00C45C2A  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
00C45C2E  48 C7 45 E0 00 02 00 00         mov qword ptr [rbp - 0x20], 0x200
00C45C36  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
00C45C3D  E8 8A AA B8 FF                  call 0x1407d06cc
00C45C42  85 C0                           test eax, eax
00C45C44  79 07                           jns 0x140c45c4d
00C45C46  48 89 1D DB 13 38 00            mov qword ptr [rip + 0x3813db], rbx
00C45C4D  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00C45C52  48 83 C4 60                     add rsp, 0x60
00C45C56  5D                              pop rbp
00C45C57  C3                              ret
00C45C58  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInitializeDesktopActivityModeratorCallouts(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    v_stack_m38 = 0x10007ULL;
    v_stack_m40 = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m20 = 0;
    v_stack_m18 = 0;
    v_stack_m28 = 512;
    v_stack_m48 = 1;
    result = ExRegisterHost(v_rip + 3675138, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 3675099) = 0;
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
void PspInitializeDesktopActivityModeratorCallouts(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    v_stack_m38 = 0x10007ULL;
    v_stack_m40 = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m20 = 0;
    v_stack_m18 = 0;
    v_stack_m28 = 512;
    v_stack_m48 = 1;
    result = ExRegisterHost(v_rip + 3675138, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x3813DB) = 0;
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C45BF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C45BF8[BB_00C45BF8]
  bb_00C45C46[BB_00C45C46]
  bb_00C45C4D[BB_00C45C4D]
  bb_00C45C58[BB_00C45C58]
  bb_00C45BF8 -->|branch| bb_00C45C4D
  bb_00C45BF8 -->|fallthrough| bb_00C45C46
  bb_00C45C46 -->|flow| bb_00C45C4D
```
