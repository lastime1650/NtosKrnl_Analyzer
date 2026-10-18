# VfAvlDeleteTreeNode

- RVA: `0x003EE240`–`0x003EE2EB` (길이 `171` bytes)
- VA: `0x00000001403EE240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000969D8`
- 디코드: `46`개 명령, `171/171` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003EE26A` → [ViAvlTableIndex](ViAvlTableIndex_function_003EF378.md) (function, `0x003EF378`)
- `0x003EE275` → [ViAvlRaiseIrqlSafe](ViAvlRaiseIrqlSafe_function_003EF404.md) (function, `0x003EF404`)
- `0x003EE28C` → [ViAvlAcquireTableLockAtDpcLevelSafe](ViAvlAcquireTableLockAtDpcLevelSafe_function_003EF3A0.md) (function, `0x003EF3A0`)
- `0x003EE29D` → [RtlDeleteElementGenericTableAvl](RtlDeleteElementGenericTableAvl_function_003EE750.md) (function, `0x003EE750`)
- `0x003EE2C0` → [ViAvlReleaseTableLockFromDpcLevel](ViAvlReleaseTableLockFromDpcLevel_function_003EF5D0.md) (function, `0x003EF5D0`)

### Direct callers
- [ViDevObjRemove](../../pagevrfy/BA/ViDevObjRemove_function_00BA248C.md) at `0x00BA2539`
- [ViRemLockDeleteFirstTreeNode](../../pagevrfy/BA/ViRemLockDeleteFirstTreeNode_function_00BA28F4.md) at `0x00BA294C`
- [VfLookasideAdd](../../pagevrfy/BA/VfLookasideAdd_function_00BAFE34.md) at `0x00BAFF01`
- [VfLookasideDelete](../../pagevrfy/BA/VfLookasideDelete_function_00BAFF58.md) at `0x00BB0006`
- [VfDeleteResource](../../pagevrfy/BB/VfDeleteResource_function_00BB187C.md) at `0x00BB1934`
- [VfTrackResource](../../pagevrfy/BB/VfTrackResource_function_00BB19A0.md) at `0x00BB1A72`
- [VfCheckForResource](../../pagevrfy/BB/VfCheckForResource_function_00BB71C8.md) at `0x00BB7296`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003EE240  48 8B C4                        mov rax, rsp
003EE243  48 89 58 08                     mov qword ptr [rax + 8], rbx
003EE247  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
003EE24B  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
003EE24F  57                              push rdi
003EE250  48 83 EC 30                     sub rsp, 0x30
003EE254  4C 89 40 E8                     mov qword ptr [rax - 0x18], r8
003EE258  48 8B EA                        mov rbp, rdx
003EE25B  48 8B F1                        mov rsi, rcx
003EE25E  4D 85 C9                        test r9, r9
003EE261  74 7B                           je 0x1403ee2de
003EE263  4C 89 48 F0                     mov qword ptr [rax - 0x10], r9
003EE267  49 8B D0                        mov rdx, r8
003EE26A  E8 09 11 00 00                  call 0x1403ef378
003EE26F  48 8B CD                        mov rcx, rbp
003EE272  48 8B D8                        mov rbx, rax
003EE275  E8 8A 11 00 00                  call 0x1403ef404
003EE27A  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
003EE27E  48 8D 3C 5B                     lea rdi, [rbx + rbx*2]
003EE282  48 C1 E7 06                     shl rdi, 6
003EE286  48 8B D5                        mov rdx, rbp
003EE289  48 03 CF                        add rcx, rdi
003EE28C  E8 0F 11 00 00                  call 0x1403ef3a0
003EE291  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
003EE295  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
003EE29A  48 03 CF                        add rcx, rdi
003EE29D  E8 AE 04 00 00                  call 0x1403ee750
003EE2A2  F0 48 FF 4E 08                  lock dec qword ptr [rsi + 8]
003EE2A7  48 8B D5                        mov rdx, rbp
003EE2AA  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
003EE2AE  48 8B 5C 0F 70                  mov rbx, qword ptr [rdi + rcx + 0x70]
003EE2B3  48 83 64 0F 70 00               and qword ptr [rdi + rcx + 0x70], 0
003EE2B9  48 8B 4E 10                     mov rcx, qword ptr [rsi + 0x10]
003EE2BD  48 03 CF                        add rcx, rdi
003EE2C0  E8 0B 13 00 00                  call 0x1403ef5d0
003EE2C5  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
003EE2CA  48 8B C3                        mov rax, rbx
003EE2CD  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
003EE2D2  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
003EE2D7  48 83 C4 30                     add rsp, 0x30
003EE2DB  5F                              pop rdi
003EE2DC  C3                              ret
003EE2DD  CC                              int3
003EE2DE  48 8B 01                        mov rax, qword ptr [rcx]
003EE2E1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003EE2E6  E9 7C FF FF FF                  jmp 0x1403ee267
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfAvlDeleteTreeNode(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = a3;
    if (a4 == 0) goto loc_003EE2DE;
    *(unsigned __int64 *)(v_rsp - 16) = a4;
loc_003EE267:
    result = ViAvlTableIndex(a1, a3, a3, a4);
    result = ViAvlRaiseIrqlSafe(a2, a3, a3, a4);
    v_rdi = (result + result * 2) << (6);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (v_rdi);
    result = ViAvlAcquireTableLockAtDpcLevelSafe(a1, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (v_rdi);
    result = RtlDeleteElementGenericTableAvl(a1, v_stack_m18, a3, a4);
    a1 = (*(unsigned __int64 *)(a1 + 16)) + (v_rdi);
    result = ViAvlReleaseTableLockFromDpcLevel(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return *(unsigned __int64 *)(v_rdi + *(unsigned __int64 *)(a1 + 16) * 1 + 112);
loc_003EE2DE:
    v_stack_p28 = *(unsigned __int64 *)(a1);
    goto loc_003EE267;
}
```

## 5. (Beta) C Style

```c
int64_t VfAvlDeleteTreeNode(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p28;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = Arg3;
    if (Arg4 == 0) goto loc_003EE2DE;
    *(uint64_t *)(local_rsp - 0x10) = Arg4;
loc_003EE267:
    result = ViAvlTableIndex(Arg1, Arg3, Arg3, Arg4);
    result = ViAvlRaiseIrqlSafe(Arg2, Arg3, Arg3, Arg4);
    local_rdi = (result + result * 2) << (6);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (local_rdi);
    result = ViAvlAcquireTableLockAtDpcLevelSafe(Arg1, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (local_rdi);
    result = RtlDeleteElementGenericTableAvl(Arg1, v_stack_m18, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) + (local_rdi);
    result = ViAvlReleaseTableLockFromDpcLevel(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return *(uint64_t *)(local_rdi + *(uint64_t *)(arg1 + 0x10) * 1 + 0x70);
loc_003EE2DE:
    v_stack_p28 = *(uint64_t *)(arg1);
    goto loc_003EE267;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003EE240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003EE240[BB_003EE240]
  bb_003EE263[BB_003EE263]
  bb_003EE267[BB_003EE267]
  bb_003EE2DD[BB_003EE2DD]
  bb_003EE2DE[BB_003EE2DE]
  bb_003EE240 -->|branch| bb_003EE2DE
  bb_003EE240 -->|fallthrough| bb_003EE263
  bb_003EE263 -->|flow| bb_003EE267
  bb_003EE2DD -->|flow| bb_003EE2DE
  bb_003EE2DE -->|branch| bb_003EE267
```
