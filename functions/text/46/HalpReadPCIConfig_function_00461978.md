# HalpReadPCIConfig

- RVA: `0x00461978`–`0x00461A02` (길이 `138` bytes)
- VA: `0x0000000140461978`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9F14`
- 디코드: `39`개 명령, `138/138` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0046199E` → [HalpValidPCISlot](HalpValidPCISlot_function_00461A08.md) (function, `0x00461A08`)
- `0x004619C9` → [HalpPCIConfig](../23/HalpPCIConfig_function_00235980.md) (function, `0x00235980`)
- `0x004619F9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [HalpSetPCIData](HalpSetPCIData_function_004615B4.md) at `0x0046161C`
- [HalpSetPCIData](HalpSetPCIData_function_004615B4.md) at `0x0046166E`
- [HalpGetPCIData](HalpGetPCIData_function_00461858.md) at `0x004618BF`
- [HalpGetPCIData](HalpGetPCIData_function_00461858.md) at `0x00461926`
- [HalpGetPCIData](HalpGetPCIData_function_00461858.md) at `0x0046195D`
- [HalpValidPCISlot](HalpValidPCISlot_function_00461A08.md) at `0x00461A69`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00461978  48 8B C4                        mov rax, rsp
0046197B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0046197F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00461983  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00461987  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0046198B  41 56                           push r14
0046198D  48 83 EC 40                     sub rsp, 0x40
00461991  49 8B F1                        mov rsi, r9
00461994  41 8B D8                        mov ebx, r8d
00461997  40 8A EA                        mov bpl, dl
0046199A  44 0F B7 F1                     movzx r14d, cx
0046199E  E8 65 00 00 00                  call 0x140461a08
004619A3  84 C0                           test al, al
004619A5  74 45                           je 0x1404619ec
004619A7  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
004619AC  4C 8B CE                        mov r9, rsi
004619AF  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
004619B3  44 8B C3                        mov r8d, ebx
004619B6  8B 7C 24 78                     mov edi, dword ptr [rsp + 0x78]
004619BA  40 8A D5                        mov dl, bpl
004619BD  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
004619C1  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
004619C5  41 0F B7 CE                     movzx ecx, r14w
004619C9  E8 B2 3F DD FF                  call 0x140235980
004619CE  8B C7                           mov eax, edi
004619D0  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
004619D5  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
004619DA  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
004619DF  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
004619E4  48 83 C4 40                     add rsp, 0x40
004619E8  41 5E                           pop r14
004619EA  C3                              ret
004619EB  CC                              int3
004619EC  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
004619F1  BA FF 00 00 00                  mov edx, 0xff
004619F6  48 8B CE                        mov rcx, rsi
004619F9  E8 42 52 26 00                  call 0x1406c6c40
004619FE  33 C0                           xor eax, eax
00461A00  EB CE                           jmp 0x1404619d0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpReadPCIConfig(unsigned __int16 a1, unsigned __int8 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = HalpValidPCISlot(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004619EC;
    v_stack_m20 = (unsigned int)((unsigned int)(a6));
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = HalpPCIConfig(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
loc_004619D0:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)(a6)));
loc_004619EC:
    result = memset(v_stack_p18, 255, (unsigned int)(a6), a4);
    result = 0;
    goto loc_004619D0;
}
```

## 5. (Beta) C Style

```c
int64_t HalpReadPCIConfig(uint16_t Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = HalpValidPCISlot(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_004619EC;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = HalpPCIConfig(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
loc_004619D0:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)(Arg6)));
loc_004619EC:
    result = memset(v_stack_p18, 255, (uint32_t)(Arg6), Arg4);
    result = 0;
    goto loc_004619D0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00461978&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00461978[BB_00461978]
  bb_004619A7[BB_004619A7]
  bb_004619D0[BB_004619D0]
  bb_004619EB[BB_004619EB]
  bb_004619EC[BB_004619EC]
  bb_00461978 -->|branch| bb_004619EC
  bb_00461978 -->|fallthrough| bb_004619A7
  bb_004619A7 -->|flow| bb_004619D0
  bb_004619EB -->|flow| bb_004619EC
  bb_004619EC -->|branch| bb_004619D0
```
