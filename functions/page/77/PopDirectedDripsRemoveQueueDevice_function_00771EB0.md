# PopDirectedDripsRemoveQueueDevice

- RVA: `0x00771EB0`–`0x00771ED9` (길이 `41` bytes)
- VA: `0x0000000140771EB0`
- 실행 섹션: `PAGE`
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
- [PopDirectedDripsBuildBroadcastTreeFull](PopDirectedDripsBuildBroadcastTreeFull_function_00771970.md) at `0x007719F2`
- [PopDirectedDripsBuildPs4BroadcastTree](PopDirectedDripsBuildPs4BroadcastTree_function_00771C90.md) at `0x00771CE4`
- [PopDirectedDripsFlushDeviceQueue](PopDirectedDripsFlushDeviceQueue_function_00771E04.md) at `0x00771E13`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00771EB0  48 8B 01                        mov rax, qword ptr [rcx]
00771EB3  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00771EB7  75 19                           jne 0x140771ed2
00771EB9  48 8B 10                        mov rdx, qword ptr [rax]
00771EBC  48 39 42 08                     cmp qword ptr [rdx + 8], rax
00771EC0  75 10                           jne 0x140771ed2
00771EC2  48 89 11                        mov qword ptr [rcx], rdx
00771EC5  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00771EC9  48 89 40 08                     mov qword ptr [rax + 8], rax
00771ECD  48 89 00                        mov qword ptr [rax], rax
00771ED0  C3                              ret
00771ED1  CC                              int3
00771ED2  B9 03 00 00 00                  mov ecx, 3
00771ED7  CD 29                           int 0x29
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDirectedDripsRemoveQueueDevice(__int64 a1)
{
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8)) != a1) goto loc_00771ED2;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8)) != (*(unsigned __int64 *)(a1))) goto loc_00771ED2;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1)) + 8) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 8) = *(unsigned __int64 *)(a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1)) = *(unsigned __int64 *)(a1);
    return *(unsigned __int64 *)(a1);
loc_00771ED2:
    return *(unsigned __int64 *)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t PopDirectedDripsRemoveQueueDevice(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if ((*(uint64_t *)(*(uint64_t *)(arg1) + 0x8)) != Arg1) goto loc_00771ED2;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8)) != (*(uint64_t *)(arg1))) goto loc_00771ED2;
    *(uint64_t *)(arg1) = *(uint64_t *)(*(uint64_t *)(arg1));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1)) + 0x8) = Arg1;
    *(uint64_t *)(*(uint64_t *)(arg1) + 0x8) = *(uint64_t *)(arg1);
    *(uint64_t *)(*(uint64_t *)(arg1)) = *(uint64_t *)(arg1);
    return *(uint64_t *)(arg1);
loc_00771ED2:
    return *(uint64_t *)(arg1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00771EB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00771EB0[BB_00771EB0]
  bb_00771EB9[BB_00771EB9]
  bb_00771EC2[BB_00771EC2]
  bb_00771ED1[BB_00771ED1]
  bb_00771ED2[BB_00771ED2]
  bb_00771EB0 -->|branch| bb_00771ED2
  bb_00771EB0 -->|fallthrough| bb_00771EB9
  bb_00771EB9 -->|branch| bb_00771ED2
  bb_00771EB9 -->|fallthrough| bb_00771EC2
  bb_00771ED1 -->|flow| bb_00771ED2
```
