# MiUpdatePagefilePeakUsage

- RVA: `0x002B54BC`–`0x002B54DF` (길이 `35` bytes)
- VA: `0x00000001402B54BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiStoreWriteModifiedPages](MiStoreWriteModifiedPages_function_002B46C4.md) at `0x002B4B6F`
- [MiGatherPagefilePages](../37/MiGatherPagefilePages_function_00372B08.md) at `0x003731C2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002B54BC  8A 81 AC 00 00 00               mov al, byte ptr [rcx + 0xac]
002B54C2  24 40                           and al, 0x40
002B54C4  F6 D8                           neg al
002B54C6  8B 01                           mov eax, dword ptr [rcx]
002B54C8  1B D2                           sbb edx, edx
002B54CA  83 E2 03                        and edx, 3
002B54CD  83 C2 02                        add edx, 2
002B54D0  2B C2                           sub eax, edx
002B54D2  2B 41 0C                        sub eax, dword ptr [rcx + 0xc]
002B54D5  39 41 10                        cmp dword ptr [rcx + 0x10], eax
002B54D8  73 03                           jae 0x1402b54dd
002B54DA  89 41 10                        mov dword ptr [rcx + 0x10], eax
002B54DD  C3                              ret
002B54DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdatePagefilePeakUsage(__int64 a1, int a2)
{
    __int64 result;

    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 172)) & (64));
    result = (unsigned __int8)(-(result));
    a2 = (unsigned int)((a2) & (3));
    a2 = (unsigned int)((a2) + (2));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (a2));
    result = (unsigned int)((result) - (*(unsigned int *)(a1 + 12)));
    if ((*(unsigned int *)(a1 + 16)) < ((unsigned int)(result))) {
        *(unsigned int *)(a1 + 16) = (unsigned int)(result);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdatePagefilePeakUsage(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = (uint8_t)((*(uint8_t *)(arg1 + 0xAC)) & (64));
    result = (uint8_t)(-(result));
    Arg2 = (uint32_t)((Arg2) & (3));
    Arg2 = (uint32_t)((Arg2) + (2));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (Arg2));
    result = (uint32_t)((result) - (*(uint32_t *)(arg1 + 0xC)));
    if ((*(uint32_t *)(arg1 + 0x10)) < ((uint32_t)(result))) {
        *(uint32_t *)(arg1 + 0x10) = (uint32_t)(result);
    }
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `W` |
| `Arg1` | `+ 0xAC` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002B54BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002B54BC[BB_002B54BC]
  bb_002B54DA[BB_002B54DA]
  bb_002B54DD[BB_002B54DD]
  bb_002B54DE[BB_002B54DE]
  bb_002B54BC -->|branch| bb_002B54DD
  bb_002B54BC -->|fallthrough| bb_002B54DA
  bb_002B54DA -->|flow| bb_002B54DD
```
