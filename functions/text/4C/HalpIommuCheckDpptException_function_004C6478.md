# HalpIommuCheckDpptException

- RVA: `0x004C6478`–`0x004C648D` (길이 `21` bytes)
- VA: `0x00000001404C6478`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalpIommuUnblockDevice](HalpIommuUnblockDevice_function_004C6250.md) at `0x004C6297`
- [HalpIommuCreateDevice](../54/HalpIommuCreateDevice_function_0054ED60.md) at `0x0054F234`

### Static image references
- `0x004C6481` → RVA `0x00FC1758` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C6478  83 39 05                        cmp dword ptr [rcx], 5
004C647B  75 04                           jne 0x1404c6481
004C647D  B0 01                           mov al, 1
004C647F  C3                              ret
004C6480  CC                              int3
004C6481  83 3D D0 B2 AF 00 01            cmp dword ptr [rip + 0xafb2d0], 1
004C6488  0F 95 C0                        setne al
004C648B  C3                              ret
004C648C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpIommuCheckDpptException(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1)) != 5) goto loc_004C6481;
    return 1;
loc_004C6481:
    result = ((*(unsigned int *)(v_rip + 11514576)) != 1) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpIommuCheckDpptException(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1)) != 5) goto loc_004C6481;
    return 1;
loc_004C6481:
    result = ((*(uint32_t *)(v_rip + 0xAFB2D0)) != 1) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C6478&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C6478[BB_004C6478]
  bb_004C647D[BB_004C647D]
  bb_004C6480[BB_004C6480]
  bb_004C6481[BB_004C6481]
  bb_004C648C[BB_004C648C]
  bb_004C6478 -->|branch| bb_004C6481
  bb_004C6478 -->|fallthrough| bb_004C647D
  bb_004C6480 -->|flow| bb_004C6481
```
