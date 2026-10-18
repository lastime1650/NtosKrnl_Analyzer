# Normalization__PageLookup

- RVA: `0x00794570`–`0x00794581` (길이 `17` bytes)
- VA: `0x0000000140794570`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [NormBuffer__GetLastChar](../../text/5E/NormBuffer__GetLastChar_function_005ED8F8.md) at `0x005ED94A`
- [NormBuffer__IsBlocked](../../text/5E/NormBuffer__IsBlocked_function_005EDA7C.md) at `0x005EDABB`
- [NormBuffer__SortBeforeSameClass](../../text/5E/NormBuffer__SortBeforeSameClass_function_005EDDF8.md) at `0x005EDE5D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00794570  48 8B 41 20                     mov rax, qword ptr [rcx + 0x20]
00794574  4C 63 C2                        movsxd r8, edx
00794577  49 C1 F8 07                     sar r8, 7
0079457B  41 8A 04 00                     mov al, byte ptr [r8 + rax]
0079457F  C3                              ret
00794580  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Normalization__PageLookup(__int64 a1, int a2)
{
    a3 = ((int)(a2)) >> (7);
    return *(unsigned __int8 *)(a3 + *(unsigned __int64 *)(a1 + 32) * 1);
}
```

## 5. (Beta) C Style

```c
int64_t Normalization__PageLookup(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    a3 = ((int32_t)(Arg2)) >> (7);
    return *(uint8_t *)(a3 + *(uint64_t *)(arg1 + 0x20) * 1);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00794570&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00794570[BB_00794570]
  bb_00794580[BB_00794580]
```
