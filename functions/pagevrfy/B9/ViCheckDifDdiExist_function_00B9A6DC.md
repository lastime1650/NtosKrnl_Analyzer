# ViCheckDifDdiExist

- RVA: `0x00B9A6DC`–`0x00B9A6F5` (길이 `25` bytes)
- VA: `0x0000000140B9A6DC`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [VfCheckDifDdiExist](VfCheckDifDdiExist_function_00B99FD0.md) at `0x00B99FDD`
- [VfCheckDifDdiExist](VfCheckDifDdiExist_function_00B99FD0.md) at `0x00B99FED`
- [VfCheckDifDdiExist](VfCheckDifDdiExist_function_00B99FD0.md) at `0x00B9A013`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9A6DC  66 90                           nop
00B9A6DE  39 51 30                        cmp dword ptr [rcx + 0x30], edx
00B9A6E1  74 0E                           je 0x140b9a6f1
00B9A6E3  48 83 C1 38                     add rcx, 0x38
00B9A6E7  48 83 39 00                     cmp qword ptr [rcx], 0
00B9A6EB  75 F1                           jne 0x140b9a6de
00B9A6ED  32 C0                           xor al, al
00B9A6EF  C3                              ret
00B9A6F0  CC                              int3
00B9A6F1  B0 01                           mov al, 1
00B9A6F3  C3                              ret
00B9A6F4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViCheckDifDdiExist(__int64 a1, int a2)
{
    __int64 result;

loc_00B9A6DE:
    if ((*(unsigned int *)(a1 + 48)) == a2) goto loc_00B9A6F1;
    a1 = (a1) + (56);
    if ((*(unsigned __int64 *)(a1)) != 0) goto loc_00B9A6DE;
    result = 0;
    return result;
loc_00B9A6F1:
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t ViCheckDifDdiExist(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

loc_00B9A6DE:
    if ((*(uint32_t *)(arg1 + 0x30)) == Arg2) goto loc_00B9A6F1;
    Arg1 = (Arg1) + (56);
    if ((*(uint64_t *)(arg1)) != 0) goto loc_00B9A6DE;
    result = 0;
    return result;
loc_00B9A6F1:
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9A6DC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9A6DC[BB_00B9A6DC]
  bb_00B9A6DE[BB_00B9A6DE]
  bb_00B9A6E3[BB_00B9A6E3]
  bb_00B9A6ED[BB_00B9A6ED]
  bb_00B9A6F0[BB_00B9A6F0]
  bb_00B9A6F1[BB_00B9A6F1]
  bb_00B9A6F4[BB_00B9A6F4]
  bb_00B9A6DC -->|flow| bb_00B9A6DE
  bb_00B9A6DE -->|branch| bb_00B9A6F1
  bb_00B9A6DE -->|fallthrough| bb_00B9A6E3
  bb_00B9A6E3 -->|branch| bb_00B9A6DE
  bb_00B9A6E3 -->|fallthrough| bb_00B9A6ED
  bb_00B9A6F0 -->|flow| bb_00B9A6F1
```
