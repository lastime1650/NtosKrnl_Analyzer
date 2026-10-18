# RtlInsertInvertedFunctionTable

- RVA: `0x00432138`–`0x004321AA` (길이 `114` bytes)
- VA: `0x0000000140432138`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2264`
- 디코드: `36`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00432160` → [RtlImageDirectoryEntryToData](RtlImageDirectoryEntryToData_function_004328D0.md) (function, `0x004328D0`)
- `0x00432174` → [MmLockLoadedModuleListExclusive](MmLockLoadedModuleListExclusive_function_0043229C.md) (function, `0x0043229C`)
- `0x00432189` → [RtlpInsertInvertedFunctionTableEntry](RtlpInsertInvertedFunctionTableEntry_function_004321B0.md) (function, `0x004321B0`)
- `0x00432191` → [MmUnlockLoadedModuleListExclusive](MmUnlockLoadedModuleListExclusive_function_004322E0.md) (function, `0x004322E0`)

### Direct callers
- [MiUpdateDriverLoadInProgress](MiUpdateDriverLoadInProgress_function_004318DC.md) at `0x00431AAA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00432138  48 8B C4                        mov rax, rsp
0043213B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0043213F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00432143  56                              push rsi
00432144  57                              push rdi
00432145  41 56                           push r14
00432147  48 83 EC 30                     sub rsp, 0x30
0043214B  83 60 18 00                     and dword ptr [rax + 0x18], 0
0043214F  4C 8D 48 18                     lea r9, [rax + 0x18]
00432153  8B EA                           mov ebp, edx
00432155  41 B8 03 00 00 00               mov r8d, 3
0043215B  B2 01                           mov dl, 1
0043215D  4C 8B F1                        mov r14, rcx
00432160  E8 6B 07 00 00                  call 0x1404328d0
00432165  4C 8B C0                        mov r8, rax
00432168  48 8B F0                        mov rsi, rax
0043216B  49 F7 D8                        neg r8
0043216E  1B DB                           sbb ebx, ebx
00432170  23 5C 24 60                     and ebx, dword ptr [rsp + 0x60]
00432174  E8 23 01 00 00                  call 0x14043229c
00432179  44 8B CD                        mov r9d, ebp
0043217C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00432180  4C 8B C6                        mov r8, rsi
00432183  49 8B D6                        mov rdx, r14
00432186  40 8A F8                        mov dil, al
00432189  E8 22 00 00 00                  call 0x1404321b0
0043218E  40 8A CF                        mov cl, dil
00432191  E8 4A 01 00 00                  call 0x1404322e0
00432196  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0043219B  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
004321A0  48 83 C4 30                     add rsp, 0x30
004321A4  41 5E                           pop r14
004321A6  5F                              pop rdi
004321A7  5E                              pop rsi
004321A8  C3                              ret
004321A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlInsertInvertedFunctionTable(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    v_rsp = (v_rsp) - (48);
    result = RtlImageDirectoryEntryToData(a1, 1, 3, v_rsp + 24);
    a3 = -(result);
    v_rbx = (unsigned int)((v_rbx) & (v_stack_p18));
    result = MmLockLoadedModuleListExclusive(a1, 1, a3, v_rsp + 24);
    v_stack_m28 = (unsigned int)(v_rbx);
    result = RtlpInsertInvertedFunctionTableEntry(a1, a1, result, (unsigned int)((unsigned int)((unsigned int)(a2))));
    result = MmUnlockLoadedModuleListExclusive((unsigned __int8)((unsigned __int8)(result)), a1, result, (unsigned int)((unsigned int)((unsigned int)(a2))));
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlInsertInvertedFunctionTable(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    local_rsp = (local_rsp) - (48);
    result = RtlImageDirectoryEntryToData(Arg1, 1, 3, local_rsp + 24);
    a3 = -(result);
    local_rbx = (uint32_t)((local_rbx) & (v_stack_p18));
    result = MmLockLoadedModuleListExclusive(Arg1, 1, a3, local_rsp + 24);
    v_stack_m28 = (uint32_t)(local_rbx);
    result = RtlpInsertInvertedFunctionTableEntry(Arg1, Arg1, result, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    result = MmUnlockLoadedModuleListExclusive((uint8_t)((uint8_t)(result)), Arg1, result, (uint32_t)((uint32_t)((uint32_t)(Arg2))));
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00432138&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00432138[BB_00432138]
  bb_004321A9[BB_004321A9]
```
