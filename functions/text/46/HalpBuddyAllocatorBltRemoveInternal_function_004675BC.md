# HalpBuddyAllocatorBltRemoveInternal

- RVA: `0x004675BC`–`0x004675E5` (길이 `41` bytes)
- VA: `0x00000001404675BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpBuddyAllocatorBltFindAndPop](HalpBuddyAllocatorBltFindAndPop_function_0046746C.md) at `0x00467504`
- [HalpBuddyAllocatorBltPopBuddy](HalpBuddyAllocatorBltPopBuddy_function_0046754C.md) at `0x004675AD`
- [HalpBuddyAllocatorBltRemove](../57/HalpBuddyAllocatorBltRemove_function_00575AC0.md) at `0x00575AE4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004675BC  48 8B 11                        mov rdx, qword ptr [rcx]
004675BF  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
004675C3  75 09                           jne 0x1404675ce
004675C5  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
004675C9  48 39 08                        cmp qword ptr [rax], rcx
004675CC  74 07                           je 0x1404675d5
004675CE  B9 03 00 00 00                  mov ecx, 3
004675D3  CD 29                           int 0x29
004675D5  48 89 10                        mov qword ptr [rax], rdx
004675D8  48 89 42 08                     mov qword ptr [rdx + 8], rax
004675DC  48 89 49 08                     mov qword ptr [rcx + 8], rcx
004675E0  48 89 09                        mov qword ptr [rcx], rcx
004675E3  C3                              ret
004675E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpBuddyAllocatorBltRemoveInternal(__int64 a1)
{
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) != a1) goto loc_004675CE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != a1) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8)) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = *(unsigned __int64 *)(a1 + 8);
    *(unsigned __int64 *)(a1 + 8) = a1;
    *(unsigned __int64 *)(a1) = a1;
    return *(unsigned __int64 *)(a1 + 8);
}
```

## 5. (Beta) C Style

```c
int64_t HalpBuddyAllocatorBltRemoveInternal(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) != Arg1) goto loc_004675CE;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != Arg1) {
        Arg1 = 3;
    }
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8)) = *(uint64_t *)(arg1);
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = *(uint64_t *)(arg1 + 0x8);
    *(void **)(arg1 + 0x8) = Arg1;
    *(void **)(arg1) = Arg1;
    return *(uint64_t *)(arg1 + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004675BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004675BC[BB_004675BC]
  bb_004675C5[BB_004675C5]
  bb_004675CE[BB_004675CE]
  bb_004675D5[BB_004675D5]
  bb_004675E4[BB_004675E4]
  bb_004675BC -->|branch| bb_004675CE
  bb_004675BC -->|fallthrough| bb_004675C5
  bb_004675C5 -->|branch| bb_004675D5
  bb_004675C5 -->|fallthrough| bb_004675CE
  bb_004675CE -->|flow| bb_004675D5
```
