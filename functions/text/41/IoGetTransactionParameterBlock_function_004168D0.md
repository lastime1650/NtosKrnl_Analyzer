# IoGetTransactionParameterBlock

- RVA: `0x004168D0`–`0x004168E4` (길이 `20` bytes)
- VA: `0x00000001404168D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36976`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A3698C`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36C81`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36C97`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36D75`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36D8B`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36F99`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A36FAF`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A3702E`
- [IopTrackLink](../../page/A3/IopTrackLink_function_00A36764.md) at `0x00A37044`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004168D0  48 8B 81 D0 00 00 00            mov rax, qword ptr [rcx + 0xd0]
004168D7  48 85 C0                        test rax, rax
004168DA  74 06                           je 0x1404168e2
004168DC  48 8B 40 08                     mov rax, qword ptr [rax + 8]
004168E0  C3                              ret
004168E1  CC                              int3
004168E2  C3                              ret
004168E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetTransactionParameterBlock(__int64 a1)
{
    if (*(unsigned __int64 *)(a1 + 208) == 0) goto loc_004168E2;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 8);
loc_004168E2:
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 208) + 8);
}
```

## 5. (Beta) C Style

```c
int64_t IoGetTransactionParameterBlock(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (*(uint64_t *)(arg1 + 0xD0) == 0) goto loc_004168E2;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x8);
loc_004168E2:
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0xD0) + 0x8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004168D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004168D0[BB_004168D0]
  bb_004168DC[BB_004168DC]
  bb_004168E1[BB_004168E1]
  bb_004168E2[BB_004168E2]
  bb_004168E3[BB_004168E3]
  bb_004168D0 -->|branch| bb_004168E2
  bb_004168D0 -->|fallthrough| bb_004168DC
  bb_004168E1 -->|flow| bb_004168E2
```
