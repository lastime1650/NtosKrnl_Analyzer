# MiUpdateSubsectionCrossPartitionRefs

- RVA: `0x004FB5DC`–`0x004FB5FC` (길이 `32` bytes)
- VA: `0x00000001404FB5DC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_002493E4](../24/Unknown_function_002493E4.md) at `0x00249424`
- [sub_0024969C](../24/Unknown_function_0024969C.md) at `0x002496E3`
- [sub_002860AF](../28/Unknown_function_002860AF.md) at `0x00286128`
- [MiFlushRelease](../29/MiFlushRelease_function_002982C0.md) at `0x00298641`
- [MiFlushRelease](../29/MiFlushRelease_function_002982C0.md) at `0x0029869B`
- [MiRemoveViewsFromSectionWithPfn](../29/MiRemoveViewsFromSectionWithPfn_function_002986D4.md) at `0x002988E1`
- [MiRemoveViewsFromSection](../29/MiRemoveViewsFromSection_function_00298960.md) at `0x00298B25`
- [MiDecrementSubsections](../29/MiDecrementSubsections_function_00298B50.md) at `0x00298D2B`
- [MiDecrementSubsectionViewCount](../29/MiDecrementSubsectionViewCount_function_00298E90.md) at `0x00298FC3`
- [sub_002E10F7](../2E/Unknown_function_002E10F7.md) at `0x002E1135`
- [MiDeleteControlArea](../36/MiDeleteControlArea_function_003691F4.md) at `0x00369368`
- [MiInsertUnusedSubsectionInternal](../67/MiInsertUnusedSubsectionInternal_function_00677EDC.md) at `0x00677FAF`
- [sub_006E1B8C](../6E/Unknown_function_006E1B8C.md) at `0x006E1BD5`
- [sub_006F4EF0](../6F/Unknown_function_006F4EF0.md) at `0x006F4EFA`
- [MiExtendSection](../../page/98/MiExtendSection_function_00982FDC.md) at `0x00983440`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FB5DC  8B C2                           mov eax, edx
004FB5DE  33 41 30                        xor eax, dword ptr [rcx + 0x30]
004FB5E1  25 00 00 00 C0                  and eax, 0xc0000000
004FB5E6  33 C2                           xor eax, edx
004FB5E8  89 41 30                        mov dword ptr [rcx + 0x30], eax
004FB5EB  81 FA FF FF FF 3F               cmp edx, 0x3fffffff
004FB5F1  75 07                           jne 0x1404fb5fa
004FB5F3  48 8B 01                        mov rax, qword ptr [rcx]
004FB5F6  80 48 3E 02                     or byte ptr [rax + 0x3e], 2
004FB5FA  C3                              ret
004FB5FB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateSubsectionCrossPartitionRefs(__int64 a1, int a2)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(a2)) ^ (*(unsigned int *)(a1 + 48)));
    result = (unsigned int)((result) & (0xC0000000ULL));
    result = (unsigned int)((result) ^ (a2));
    *(unsigned int *)(a1 + 48) = (unsigned int)(result);
    if (a2 == 0x3FFFFFFFULL) {
        result = *(unsigned __int64 *)(a1);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdateSubsectionCrossPartitionRefs(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint32_t)(((uint32_t)(Arg2)) ^ (*(uint32_t *)(arg1 + 0x30)));
    result = (uint32_t)((result) & (0xC0000000ULL));
    result = (uint32_t)((result) ^ (Arg2));
    *(uint32_t *)(arg1 + 0x30) = (uint32_t)(result);
    if (Arg2 == 0x3FFFFFFFULL) {
        result = *(uint64_t *)(arg1);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FB5DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FB5DC[BB_004FB5DC]
  bb_004FB5F3[BB_004FB5F3]
  bb_004FB5FA[BB_004FB5FA]
  bb_004FB5FB[BB_004FB5FB]
  bb_004FB5DC -->|branch| bb_004FB5FA
  bb_004FB5DC -->|fallthrough| bb_004FB5F3
  bb_004FB5F3 -->|flow| bb_004FB5FA
```
