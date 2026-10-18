# MiLockHugePfn

- RVA: `0x006765FC`–`0x0067663C` (길이 `64` bytes)
- VA: `0x00000001406765FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `19`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00676621` → [KiRaiseIrqlProcessIrqlFlags](../4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x00676629` → [MiLockHugePfnInternal](../3F/MiLockHugePfnInternal_function_003FBC80.md) (function, `0x003FBC80`)

### Direct callers
- [MiGetHugeRange](MiGetHugeRange_function_00675954.md) at `0x00675A90`
- [MiGetPageInHugePageBadStatus](MiGetPageInHugePageBadStatus_function_00675ADC.md) at `0x00675B37`
- [MiHotRemoveHugeRange](MiHotRemoveHugeRange_function_00675DD0.md) at `0x00675E62`
- [MiMarkHugePfnBad](MiMarkHugePfnBad_function_00676744.md) at `0x0067685D`
- [MiMarkHugePfnGood](MiMarkHugePfnGood_function_00676BB0.md) at `0x00676BFB`
- [MiMoveBadHugeRangeCrossPartition](MiMoveBadHugeRangeCrossPartition_function_00676DD0.md) at `0x00676E0E`
- [MiReleaseMemoryRuns](MiReleaseMemoryRuns_function_00676EF0.md) at `0x00676FBA`
- [MiUpdateBadPfnIdentity](MiUpdateBadPfnIdentity_function_0067A890.md) at `0x0067A8E7`
- [MiInsertHugeRangeInPartition](../69/MiInsertHugeRangeInPartition_function_00690F28.md) at `0x00690F59`

### Static image references
- `0x00676616` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006765FC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00676601  57                              push rdi
00676602  48 83 EC 20                     sub rsp, 0x20
00676606  48 8B F9                        mov rdi, rcx
00676609  44 0F 20 C3                     mov rbx, cr8
0067660D  BA 02 00 00 00                  mov edx, 2
00676612  44 0F 22 C2                     mov cr8, rdx
00676616  83 3D 03 07 95 00 00            cmp dword ptr [rip + 0x950703], 0
0067661D  74 07                           je 0x140676626
0067661F  8A CB                           mov cl, bl
00676621  E8 D6 F0 E7 FF                  call 0x1404f56fc
00676626  48 8B CF                        mov rcx, rdi
00676629  E8 52 56 D8 FF                  call 0x1403fbc80
0067662E  8A C3                           mov al, bl
00676630  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00676635  48 83 C4 20                     add rsp, 0x20
00676639  5F                              pop rdi
0067663A  C3                              ret
0067663B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockHugePfn(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    if ((*(unsigned int *)(v_rip + 9766659)) != 0) {
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, 2, a3, a4);
    }
    result = MiLockHugePfnInternal(a1, 2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_cr8);
}
```

## 5. (Beta) C Style

```c
int64_t MiLockHugePfn(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    if ((*(uint32_t *)(v_rip + 0x950703)) != 0) {
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, 2, a3, a4);
    }
    result = MiLockHugePfnInternal(Arg1, 2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(v_cr8);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006765FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006765FC[BB_006765FC]
  bb_0067661F[BB_0067661F]
  bb_00676626[BB_00676626]
  bb_0067663B[BB_0067663B]
  bb_006765FC -->|branch| bb_00676626
  bb_006765FC -->|fallthrough| bb_0067661F
  bb_0067661F -->|flow| bb_00676626
```
