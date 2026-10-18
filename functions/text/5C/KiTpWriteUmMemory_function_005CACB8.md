# KiTpWriteUmMemory

- RVA: `0x005CACB8`–`0x005CAD83` (길이 `203` bytes)
- VA: `0x00000001405CACB8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CB2F0`
- 디코드: `57`개 명령, `203/203` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CAD14` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (function, `0x00881050`)
- `0x005CAD42` → [MmCopyVirtualMemory](../../page/9B/MmCopyVirtualMemory_function_009BBB10.md) (function, `0x009BBB10`)
- `0x005CAD67` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (function, `0x00881050`)

### Direct callers
- [KiTpWriteMemory](KiTpWriteMemory_function_005CAB94.md) at `0x005CABF5`

### Static image references
- `0x005CACD0` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x005CAD14` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (`.text` → `PAGE`)
  - `0x005CAD42` → [MmCopyVirtualMemory](../../page/9B/MmCopyVirtualMemory_function_009BBB10.md) (`.text` → `PAGE`)
  - `0x005CAD67` → [MmProtectVirtualMemory](../../page/88/MmProtectVirtualMemory_function_00881050.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CACB8  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
005CACBD  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
005CACC2  55                              push rbp
005CACC3  56                              push rsi
005CACC4  57                              push rdi
005CACC5  41 56                           push r14
005CACC7  41 57                           push r15
005CACC9  48 8B EC                        mov rbp, rsp
005CACCC  48 83 EC 50                     sub rsp, 0x50
005CACD0  48 8B 35 D9 BD 9F 00            mov rsi, qword ptr [rip + 0x9fbdd9]
005CACD7  48 8D 45 48                     lea rax, [rbp + 0x48]
005CACDB  48 83 65 F0 00                  and qword ptr [rbp - 0x10], 0
005CACE0  4C 8D 4D 30                     lea r9, [rbp + 0x30]
005CACE4  83 65 48 00                     and dword ptr [rbp + 0x48], 0
005CACE8  4C 8B F2                        mov r14, rdx
005CACEB  48 89 55 38                     mov qword ptr [rbp + 0x38], rdx
005CACEF  4D 8B F8                        mov r15, r8
005CACF2  48 8B D1                        mov rdx, rcx
005CACF5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005CACFA  48 8B F9                        mov rdi, rcx
005CACFD  C7 44 24 20 80 00 00 00         mov dword ptr [rsp + 0x20], 0x80
005CAD05  48 8B CE                        mov rcx, rsi
005CAD08  48 C7 45 30 01 00 00 00         mov qword ptr [rbp + 0x30], 1
005CAD10  4C 8D 45 38                     lea r8, [rbp + 0x38]
005CAD14  E8 37 63 2B 00                  call 0x140881050
005CAD19  8B D8                           mov ebx, eax
005CAD1B  85 C0                           test eax, eax
005CAD1D  78 4D                           js 0x1405cad6c
005CAD1F  48 8D 45 F0                     lea rax, [rbp - 0x10]
005CAD23  4D 8B CE                        mov r9, r14
005CAD26  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005CAD2B  4C 8B C7                        mov r8, rdi
005CAD2E  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
005CAD33  49 8B D7                        mov rdx, r15
005CAD36  48 8B CE                        mov rcx, rsi
005CAD39  48 C7 44 24 20 01 00 00 00      mov qword ptr [rsp + 0x20], 1
005CAD42  E8 C9 0D 3F 00                  call 0x1409bbb10
005CAD47  8B D8                           mov ebx, eax
005CAD49  4C 8D 4D 30                     lea r9, [rbp + 0x30]
005CAD4D  48 8D 45 48                     lea rax, [rbp + 0x48]
005CAD51  48 8B D7                        mov rdx, rdi
005CAD54  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005CAD59  4C 8D 45 38                     lea r8, [rbp + 0x38]
005CAD5D  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
005CAD60  48 8B CE                        mov rcx, rsi
005CAD63  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005CAD67  E8 E4 62 2B 00                  call 0x140881050
005CAD6C  8B C3                           mov eax, ebx
005CAD6E  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
005CAD76  48 83 C4 50                     add rsp, 0x50
005CAD7A  41 5F                           pop r15
005CAD7C  41 5E                           pop r14
005CAD7E  5F                              pop rdi
005CAD7F  5E                              pop rsi
005CAD80  5D                              pop rbp
005CAD81  C3                              ret
005CAD82  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiTpWriteUmMemory(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (80);
    v_stack_p10 = a2;
    v_stack_m50 = v_stack_p20;
    v_stack_m58 = 128;
    v_stack_p8 = 1;
    result = MmProtectVirtualMemory(*(unsigned __int64 *)(v_rip + 10468825), a1, v_stack_p10, v_stack_p8);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        result = v_stack_m38;
        a4 = a2;
        v_stack_m48 = result;
        a3 = a1;
        v_stack_m50 = 0;
        a2 = a3;
        a1 = *(unsigned __int64 *)(v_rip + 10468825);
        v_stack_m58 = 1;
        result = MmCopyVirtualMemory(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
        a4 = v_stack_p8;
        result = v_stack_p20;
        a2 = a1;
        v_stack_m50 = result;
        a3 = v_stack_p10;
        result = v_stack_p20;
        a1 = *(unsigned __int64 *)(v_rip + 10468825);
        v_stack_m58 = (unsigned int)(result);
        result = MmProtectVirtualMemory(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t KiTpWriteUmMemory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (80);
    v_stack_p10 = Arg2;
    v_stack_m50 = v_stack_p20;
    v_stack_m58 = 128;
    v_stack_p8 = 1;
    result = MmProtectVirtualMemory(*(uint64_t *)(v_rip + 0x9FBDD9), Arg1, v_stack_p10, v_stack_p8);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        result = v_stack_m38;
        Arg4 = Arg2;
        v_stack_m48 = result;
        Arg3 = Arg1;
        v_stack_m50 = 0;
        Arg2 = Arg3;
        Arg1 = *(uint64_t *)(v_rip + 0x9FBDD9);
        v_stack_m58 = 1;
        result = MmCopyVirtualMemory(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
        Arg4 = v_stack_p8;
        result = v_stack_p20;
        Arg2 = Arg1;
        v_stack_m50 = result;
        Arg3 = v_stack_p10;
        result = v_stack_p20;
        Arg1 = *(uint64_t *)(v_rip + 0x9FBDD9);
        v_stack_m58 = (uint32_t)(result);
        result = MmProtectVirtualMemory(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CACB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CACB8[BB_005CACB8]
  bb_005CAD1F[BB_005CAD1F]
  bb_005CAD6C[BB_005CAD6C]
  bb_005CAD82[BB_005CAD82]
  bb_005CACB8 -->|branch| bb_005CAD6C
  bb_005CACB8 -->|fallthrough| bb_005CAD1F
  bb_005CAD1F -->|flow| bb_005CAD6C
```
