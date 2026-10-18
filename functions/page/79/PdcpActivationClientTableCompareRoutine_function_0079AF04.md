# PdcpActivationClientTableCompareRoutine

- RVA: `0x0079AF04`–`0x0079AF22` (길이 `30` bytes)
- VA: `0x000000014079AF04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [Pdcv2pActivationClientCallback](Pdcv2pActivationClientCallback_function_0079B2C0.md) at `0x0079B390`
- [Pdcv2ActivationClientActivate](../95/Pdcv2ActivationClientActivate_function_00953C70.md) at `0x00953F88`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079AF04  4C 8B 01                        mov r8, qword ptr [rcx]
0079AF07  48 8B 8A 58 02 00 00            mov rcx, qword ptr [rdx + 0x258]
0079AF0E  4C 3B C1                        cmp r8, rcx
0079AF11  73 05                           jae 0x14079af18
0079AF13  83 C8 FF                        or eax, 0xffffffff
0079AF16  C3                              ret
0079AF17  CC                              int3
0079AF18  33 C0                           xor eax, eax
0079AF1A  4C 3B C1                        cmp r8, rcx
0079AF1D  0F 95 C0                        setne al
0079AF20  C3                              ret
0079AF21  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PdcpActivationClientTableCompareRoutine(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned __int64 *)(a1)) >= (*(unsigned __int64 *)(a2 + 600))) goto loc_0079AF18;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
loc_0079AF18:
    result = 0;
    result = ((*(unsigned __int64 *)(a1)) != (*(unsigned __int64 *)(a2 + 600))) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PdcpActivationClientTableCompareRoutine(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint64_t *)(arg1)) >= (*(uint64_t *)(arg2 + 0x258))) goto loc_0079AF18;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
loc_0079AF18:
    result = 0;
    result = ((*(uint64_t *)(arg1)) != (*(uint64_t *)(arg2 + 0x258))) ? 1 : 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x258` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079AF04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079AF04[BB_0079AF04]
  bb_0079AF13[BB_0079AF13]
  bb_0079AF17[BB_0079AF17]
  bb_0079AF18[BB_0079AF18]
  bb_0079AF21[BB_0079AF21]
  bb_0079AF04 -->|branch| bb_0079AF18
  bb_0079AF04 -->|fallthrough| bb_0079AF13
  bb_0079AF17 -->|flow| bb_0079AF18
```
