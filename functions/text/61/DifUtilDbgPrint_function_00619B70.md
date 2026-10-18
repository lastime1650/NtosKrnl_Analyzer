# DifUtilDbgPrint

- RVA: `0x00619B70`–`0x00619BC4` (길이 `84` bytes)
- VA: `0x0000000140619B70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CF7BC`
- 디코드: `22`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00619BB9` → [vDbgPrintExWithPrefixInternal](../35/vDbgPrintExWithPrefixInternal_function_00359314.md) (function, `0x00359314`)

### Direct callers
- [DifCallPluginEntry](DifCallPluginEntry_function_0061A5A0.md) at `0x0061A63B`
- [DifRegisterKernelPlugins](DifRegisterKernelPlugins_function_0061AA40.md) at `0x0061AB85`

### Static image references
- `0x00619B87` → RVA `0x00E681A0` (`.data`; read)
- `0x00619BAA` → RVA `0x006C7800` (` ?? ::FNODOBFM::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00619B70  4C 8B DC                        mov r11, rsp
00619B73  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
00619B77  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
00619B7B  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
00619B7F  4D 89 4B 20                     mov qword ptr [r11 + 0x20], r9
00619B83  48 83 EC 48                     sub rsp, 0x48
00619B87  F7 05 0F E6 84 00 00 00 40 00   test dword ptr [rip + 0x84e60f], 0x400000
00619B91  75 2B                           jne 0x140619bbe
00619B93  44 0F 20 C0                     mov rax, cr8
00619B97  84 C0                           test al, al
00619B99  75 23                           jne 0x140619bbe
00619B9B  45 33 C0                        xor r8d, r8d
00619B9E  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00619BA3  49 8D 43 10                     lea rax, [r11 + 0x10]
00619BA7  4C 8B C9                        mov r9, rcx
00619BAA  48 8D 0D 4F DC 0A 00            lea rcx, [rip + 0xadc4f]
00619BB1  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00619BB5  41 8D 50 65                     lea edx, [r8 + 0x65]
00619BB9  E8 56 F7 D3 FF                  call 0x140359314
00619BBE  48 83 C4 48                     add rsp, 0x48
00619BC2  C3                              ret
00619BC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifUtilDbgPrint(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m20;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (72);
    if (((*(unsigned int *)(v_rip + 8709647)) & (0x400000ULL)) != 0) goto loc_00619BBE;
    result = v_cr8;
    if ((unsigned __int8)(v_cr8) == 0) {
        a3 = 0;
        v_stack_m20 = 1;
        result = v_rsp + 16;
        a4 = a1;
        a1 = v_rip + 711759;
        *(unsigned __int64 *)(v_rsp - 40) = result;
        a2 = a3 + 101;
        result = vDbgPrintExWithPrefixInternal(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DifUtilDbgPrint(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m20;

    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (72);
    if (((*(uint32_t *)(v_rip + 0x84E60F)) & (0x400000ULL)) != 0) goto loc_00619BBE;
    result = v_cr8;
    if ((uint8_t)(v_cr8) == 0) {
        Arg3 = 0;
        v_stack_m20 = 1;
        result = local_rsp + 16;
        Arg4 = Arg1;
        Arg1 = v_rip + 711759;
        *(uint64_t *)(local_rsp - 0x28) = result;
        Arg2 = Arg3 + 101;
        result = vDbgPrintExWithPrefixInternal(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00619B70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00619B70[BB_00619B70]
  bb_00619B93[BB_00619B93]
  bb_00619B9B[BB_00619B9B]
  bb_00619BBE[BB_00619BBE]
  bb_00619BC3[BB_00619BC3]
  bb_00619B70 -->|branch| bb_00619BBE
  bb_00619B70 -->|fallthrough| bb_00619B93
  bb_00619B93 -->|branch| bb_00619BBE
  bb_00619B93 -->|fallthrough| bb_00619B9B
  bb_00619B9B -->|flow| bb_00619BBE
```
