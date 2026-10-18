# PopGenerateMdl

- RVA: `0x003EBC70`–`0x003EBD05` (길이 `149` bytes)
- VA: `0x00000001403EBC70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E5F8`
- 디코드: `37`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003EBCA9` → [MmAllocatePagesForMdlEx](MmAllocatePagesForMdlEx_function_003EA8C0.md) (function, `0x003EA8C0`)

### Direct callers
- [PopAllocatePages](../../pagelk/B7/PopAllocatePages_function_00B7E3FC.md) at `0x00B7E40A`

### Static image references
- `0x003EBCB6` → RVA `0x00F0BD90` (`.data`; read)
- `0x003EBCF4` → RVA `0x00F0C388` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EBC70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
003EBC75  57                              push rdi
003EBC76  48 83 EC 30                     sub rsp, 0x30
003EBC7A  48 8B D9                        mov rbx, rcx
003EBC7D  0F 31                           rdtsc
003EBC7F  48 C1 E2 20                     shl rdx, 0x20
003EBC83  4C 8B C9                        mov r9, rcx
003EBC86  48 0B C2                        or rax, rdx
003EBC89  49 C1 E1 0C                     shl r9, 0xc
003EBC8D  48 83 CA FF                     or rdx, 0xffffffffffffffff
003EBC91  C7 44 24 28 0D 00 00 00         mov dword ptr [rsp + 0x28], 0xd
003EBC99  45 33 C0                        xor r8d, r8d
003EBC9C  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
003EBCA4  33 C9                           xor ecx, ecx
003EBCA6  48 8B F8                        mov rdi, rax
003EBCA9  E8 12 EC FF FF                  call 0x1403ea8c0
003EBCAE  4C 8B C0                        mov r8, rax
003EBCB1  48 85 C0                        test rax, rax
003EBCB4  74 2D                           je 0x1403ebce3
003EBCB6  48 8B 0D D3 00 B2 00            mov rcx, qword ptr [rip + 0xb200d3]
003EBCBD  48 8B 91 90 00 00 00            mov rdx, qword ptr [rcx + 0x90]
003EBCC4  48 89 10                        mov qword ptr [rax], rdx
003EBCC7  48 8B 0D C2 00 B2 00            mov rcx, qword ptr [rip + 0xb200c2]
003EBCCE  48 89 81 90 00 00 00            mov qword ptr [rcx + 0x90], rax
003EBCD5  48 8B 0D B4 00 B2 00            mov rcx, qword ptr [rip + 0xb200b4]
003EBCDC  48 01 99 98 00 00 00            add qword ptr [rcx + 0x98], rbx
003EBCE3  0F 31                           rdtsc
003EBCE5  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003EBCEA  48 C1 E2 20                     shl rdx, 0x20
003EBCEE  48 0B C2                        or rax, rdx
003EBCF1  48 2B C7                        sub rax, rdi
003EBCF4  48 01 05 8D 06 B2 00            add qword ptr [rip + 0xb2068d], rax
003EBCFB  49 8B C0                        mov rax, r8
003EBCFE  48 83 C4 30                     add rsp, 0x30
003EBD02  5F                              pop rdi
003EBD03  C3                              ret
003EBD04  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopGenerateMdl(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (48);
    a2 = (a2) << (32);
    result = (result) | (a2);
    a4 = (a1) << (12);
    a2 = (a2) | (-1);
    v_stack_m10 = 13;
    a3 = 0;
    v_stack_m18 = 1;
    a1 = 0;
    result = MmAllocatePagesForMdlEx(a1, a2, a3, a4);
    if (result != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 11665619);
        a2 = *(unsigned __int64 *)(a1 + 144);
        *(unsigned __int64 *)(result) = a2;
        a1 = *(unsigned __int64 *)(v_rip + 11665602);
        *(unsigned __int64 *)(a1 + 144) = result;
        a1 = *(unsigned __int64 *)(v_rip + 11665588);
    }
    a2 = (a2) << (32);
    result = (result) | (a2);
    result = (result) - (result);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopGenerateMdl(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (48);
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    a4 = (Arg1) << (12);
    Arg2 = (Arg2) | (-1);
    v_stack_m10 = 13;
    Arg3 = 0;
    v_stack_m18 = 1;
    Arg1 = 0;
    result = MmAllocatePagesForMdlEx(Arg1, Arg2, Arg3, a4);
    if (result != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0xB200D3);
        Arg2 = *(uint64_t *)(Arg1 + 0x90);
        *(uint64_t *)(result) = Arg2;
        Arg1 = *(uint64_t *)(v_rip + 0xB200C2);
        *(uint64_t *)(Arg1 + 0x90) = result;
        Arg1 = *(uint64_t *)(v_rip + 0xB200B4);
    }
    Arg2 = (Arg2) << (32);
    result = (result) | (Arg2);
    result = (result) - (result);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EBC70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EBC70[BB_003EBC70]
  bb_003EBCB6[BB_003EBCB6]
  bb_003EBCE3[BB_003EBCE3]
  bb_003EBD04[BB_003EBD04]
  bb_003EBC70 -->|branch| bb_003EBCE3
  bb_003EBC70 -->|fallthrough| bb_003EBCB6
  bb_003EBCB6 -->|flow| bb_003EBCE3
```
