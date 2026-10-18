# MiVadBitToUserVa

- RVA: `0x009D60D0`–`0x009D60E5` (길이 `21` bytes)
- VA: `0x00000001409D60D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiClearVadCellBits](../../text/29/MiClearVadCellBits_function_0029753C.md) at `0x00297566`

### Static image references
- `0x009D60D4` → RVA `0x00E2F388` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009D60D0  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009D60D4  48 2B 05 AD 92 45 00            sub rax, qword ptr [rip + 0x4592ad]
009D60DB  48 8D 04 C2                     lea rax, [rdx + rax*8]
009D60DF  48 C1 E0 10                     shl rax, 0x10
009D60E3  C3                              ret
009D60E4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiVadBitToUserVa(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (*(unsigned __int64 *)(a1 + 8)) - (*(unsigned __int64 *)(v_rip + 4559533));
    result = (a2 + result * 8) << (16);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiVadBitToUserVa(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (*(uint64_t *)(arg1 + 0x8)) - (*(uint64_t *)(v_rip + 0x4592AD));
    result = (Arg2 + result * 8) << (16);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x0 + rax*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D60D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009D60D0[BB_009D60D0]
  bb_009D60E4[BB_009D60E4]
```
