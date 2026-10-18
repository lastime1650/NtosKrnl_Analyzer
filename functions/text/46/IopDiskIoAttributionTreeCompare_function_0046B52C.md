# IopDiskIoAttributionTreeCompare

- RVA: `0x0046B52C`–`0x0046B547` (길이 `27` bytes)
- VA: `0x000000014046B52C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IoStartDiskIoAttributionForContext](IoStartDiskIoAttributionForContext_function_0046B434.md) at `0x0046B495`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0046B52C  4C 8B 01                        mov r8, qword ptr [rcx]
0046B52F  48 8B 4A 18                     mov rcx, qword ptr [rdx + 0x18]
0046B533  4C 3B C1                        cmp r8, rcx
0046B536  72 0A                           jb 0x14046b542
0046B538  33 C0                           xor eax, eax
0046B53A  4C 3B C1                        cmp r8, rcx
0046B53D  0F 97 C0                        seta al
0046B540  C3                              ret
0046B541  CC                              int3
0046B542  83 C8 FF                        or eax, 0xffffffff
0046B545  C3                              ret
0046B546  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopDiskIoAttributionTreeCompare(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a1)) < (*(unsigned __int64 *)(a2 + 24))) goto loc_0046B542;
    result = 0;
    result = ((*(unsigned __int64 *)(a1)) > (*(unsigned __int64 *)(a2 + 24))) ? 1 : 0;
    return result;
loc_0046B542:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopDiskIoAttributionTreeCompare(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint64_t *)(arg1)) < (*(uint64_t *)(arg2 + 0x18))) goto loc_0046B542;
    result = 0;
    result = ((*(uint64_t *)(arg1)) > (*(uint64_t *)(arg2 + 0x18))) ? 1 : 0;
    return result;
loc_0046B542:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0046B52C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0046B52C[BB_0046B52C]
  bb_0046B538[BB_0046B538]
  bb_0046B541[BB_0046B541]
  bb_0046B542[BB_0046B542]
  bb_0046B546[BB_0046B546]
  bb_0046B52C -->|branch| bb_0046B542
  bb_0046B52C -->|fallthrough| bb_0046B538
  bb_0046B541 -->|flow| bb_0046B542
```
