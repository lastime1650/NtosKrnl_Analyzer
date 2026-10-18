# PiIommuIsPassthroughAllowedWhileConsoleLocked

- RVA: `0x00740254`–`0x00740266` (길이 `18` bytes)
- VA: `0x0000000140740254`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PipDmgEnforceEnumerationPolicy](../73/PipDmgEnforceEnumerationPolicy_function_0073BEB4.md) at `0x0073BF09`
- [PipDmgEnforceEnumerationPolicy](../73/PipDmgEnforceEnumerationPolicy_function_0073BEB4.md) at `0x0073BF2D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00740254  8A 41 10                        mov al, byte ptr [rcx + 0x10]
00740257  A8 08                           test al, 8
00740259  75 07                           jne 0x140740262
0074025B  A8 24                           test al, 0x24
0074025D  0F 94 C0                        sete al
00740260  C3                              ret
00740261  CC                              int3
00740262  B0 01                           mov al, 1
00740264  C3                              ret
00740265  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiIommuIsPassthroughAllowedWhileConsoleLocked(__int64 a1)
{
    __int64 result;

    if ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 16))) & (8)) != 0) goto loc_00740262;
    result = ((((unsigned __int8)(*(unsigned __int8 *)(a1 + 16))) & (36)) == 0) ? 1 : 0;
    return result;
loc_00740262:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t PiIommuIsPassthroughAllowedWhileConsoleLocked(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((((uint8_t)(*(uint8_t *)(arg1 + 0x10))) & (8)) != 0) goto loc_00740262;
    result = ((((uint8_t)(*(uint8_t *)(arg1 + 0x10))) & (36)) == 0) ? 1 : 0;
    return result;
loc_00740262:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00740254&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00740254[BB_00740254]
  bb_0074025B[BB_0074025B]
  bb_00740261[BB_00740261]
  bb_00740262[BB_00740262]
  bb_00740265[BB_00740265]
  bb_00740254 -->|branch| bb_00740262
  bb_00740254 -->|fallthrough| bb_0074025B
  bb_00740261 -->|flow| bb_00740262
```
