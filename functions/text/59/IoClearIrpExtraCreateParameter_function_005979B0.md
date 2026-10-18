# IoClearIrpExtraCreateParameter

- RVA: `0x005979B0`–`0x005979BE` (길이 `14` bytes)
- VA: `0x00000001405979B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `14/14` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00B19BDE](../../page/B1/Unknown_function_00B19BDE.md) at `0x00B19BF2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005979B0  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
005979B3  84 C0                           test al, al
005979B5  79 05                           jns 0x1405979bc
005979B7  48 83 61 70 00                  and qword ptr [rcx + 0x70], 0
005979BC  C3                              ret
005979BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoClearIrpExtraCreateParameter(__int64 a1)
{
    if (sign_flag) {
    }
    return (unsigned int)(*(unsigned int *)(a1 + 16));
}
```

## 5. (Beta) C Style

```c
int64_t IoClearIrpExtraCreateParameter(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    if (sign_flag) {
    }
    return (uint32_t)(*(uint32_t *)(arg1 + 0x10));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005979B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005979B0[BB_005979B0]
  bb_005979B7[BB_005979B7]
  bb_005979BC[BB_005979BC]
  bb_005979BD[BB_005979BD]
  bb_005979B0 -->|branch| bb_005979BC
  bb_005979B0 -->|fallthrough| bb_005979B7
  bb_005979B7 -->|flow| bb_005979BC
```
