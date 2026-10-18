# MiInsertHugeRangeInPartition

- RVA: `0x00690F28`–`0x00690F8E` (길이 `102` bytes)
- VA: `0x0000000140690F28`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C954`
- 디코드: `28`개 명령, `102/102` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00690F59` → [MiLockHugePfn](../67/MiLockHugePfn_function_006765FC.md) (function, `0x006765FC`)
- `0x00690F68` → [MiInsertHugeRangeInList](../43/MiInsertHugeRangeInList_function_004371E8.md) (function, `0x004371E8`)
- `0x00690F73` → [MiUnlockHugePfn](../4D/MiUnlockHugePfn_function_004D90E4.md) (function, `0x004D90E4`)

### Direct callers
- [MiFreePartitionPageRun](MiFreePartitionPageRun_function_00690DA0.md) at `0x00690E24`
- [MiInsertPartitionPages](MiInsertPartitionPages_function_006911A0.md) at `0x00691400`
- [MiInsertPartitionPages](MiInsertPartitionPages_function_006911A0.md) at `0x00691577`
- [MiAllocatePartitionPhysicalPages](../../page/80/MiAllocatePartitionPhysicalPages_function_0080C9D4.md) at `0x0080CDD4`

### Static image references
- `0x00690F3C` → RVA `0x00E300C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00690F28  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00690F2D  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
00690F32  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
00690F37  57                              push rdi
00690F38  48 83 EC 20                     sub rsp, 0x20
00690F3C  48 8B 05 7D F1 79 00            mov rax, qword ptr [rip + 0x79f17d]
00690F43  48 8B F9                        mov rdi, rcx
00690F46  48 C1 EF 12                     shr rdi, 0x12
00690F4A  8B DA                           mov ebx, edx
00690F4C  81 E7 FF FF 3F 00               and edi, 0x3fffff
00690F52  48 8D 2C F8                     lea rbp, [rax + rdi*8]
00690F56  48 8B CD                        mov rcx, rbp
00690F59  E8 9E 56 FE FF                  call 0x1406765fc
00690F5E  44 8B C3                        mov r8d, ebx
00690F61  8B D7                           mov edx, edi
00690F63  33 C9                           xor ecx, ecx
00690F65  40 8A F0                        mov sil, al
00690F68  E8 7B 62 DA FF                  call 0x1404371e8
00690F6D  40 8A D6                        mov dl, sil
00690F70  48 8B CD                        mov rcx, rbp
00690F73  E8 6C 81 E4 FF                  call 0x1404d90e4
00690F78  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00690F7D  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
00690F82  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00690F87  48 83 C4 20                     add rsp, 0x20
00690F8B  5F                              pop rdi
00690F8C  C3                              ret
00690F8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInsertHugeRangeInPartition(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = (a1) >> (18);
    v_rdi = (unsigned int)((v_rdi) & (0x3FFFFFULL));
    result = MiLockHugePfn(*(unsigned __int64 *)(v_rip + 7991677) + v_rdi * 8, a2, a3, a4);
    a1 = 0;
    result = MiInsertHugeRangeInList(a1, (unsigned int)((unsigned int)(v_rdi)), (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    result = MiUnlockHugePfn(*(unsigned __int64 *)(v_rip + 7991677) + v_rdi * 8, (unsigned __int8)((unsigned __int8)(result)), (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInsertHugeRangeInPartition(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = (Arg1) >> (18);
    local_rdi = (uint32_t)((local_rdi) & (0x3FFFFFULL));
    result = MiLockHugePfn(*(uint64_t *)(v_rip + 0x79F17D) + local_rdi * 8, Arg2, a3, a4);
    Arg1 = 0;
    result = MiInsertHugeRangeInList(Arg1, (uint32_t)((uint32_t)(local_rdi)), (uint32_t)((uint32_t)((uint32_t)(Arg2))), a4);
    result = MiUnlockHugePfn(*(uint64_t *)(v_rip + 0x79F17D) + local_rdi * 8, (uint8_t)((uint8_t)(result)), (uint32_t)((uint32_t)((uint32_t)(Arg2))), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00690F28&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00690F28[BB_00690F28]
  bb_00690F8D[BB_00690F8D]
```
