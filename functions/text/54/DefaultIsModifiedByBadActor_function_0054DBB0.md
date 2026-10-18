# DefaultIsModifiedByBadActor

- RVA: `0x0054DBB0`–`0x0054DBCF` (길이 `31` bytes)
- VA: `0x000000014054DBB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `14`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054DBB0  83 FA 01                        cmp edx, 1
0054DBB3  74 07                           je 0x14054dbbc
0054DBB5  B8 F0 00 00 C0                  mov eax, 0xc00000f0
0054DBBA  C3                              ret
0054DBBB  CC                              int3
0054DBBC  85 C9                           test ecx, ecx
0054DBBE  74 07                           je 0x14054dbc7
0054DBC0  B8 EF 00 00 C0                  mov eax, 0xc00000ef
0054DBC5  C3                              ret
0054DBC6  CC                              int3
0054DBC7  41 C6 00 00                     mov byte ptr [r8], 0
0054DBCB  33 C0                           xor eax, eax
0054DBCD  C3                              ret
0054DBCE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DefaultIsModifiedByBadActor(int a1, int a2, __int64 a3)
{
    __int64 result;

    if (a2 == 1) goto loc_0054DBBC;
    return (unsigned int)(0xC00000F0ULL);
loc_0054DBBC:
    if (a1 == 0) goto loc_0054DBC7;
    return (unsigned int)(0xC00000EFULL);
loc_0054DBC7:
    *(unsigned __int8 *)(a3) = 0;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DefaultIsModifiedByBadActor(int32_t Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (Arg2 == 1) goto loc_0054DBBC;
    return (uint32_t)(0xC00000F0ULL);
loc_0054DBBC:
    if (Arg1 == 0) goto loc_0054DBC7;
    return (uint32_t)(0xC00000EFULL);
loc_0054DBC7:
    *(uint8_t *)(arg3) = 0;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054DBB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054DBB0[BB_0054DBB0]
  bb_0054DBB5[BB_0054DBB5]
  bb_0054DBBB[BB_0054DBBB]
  bb_0054DBBC[BB_0054DBBC]
  bb_0054DBC0[BB_0054DBC0]
  bb_0054DBC6[BB_0054DBC6]
  bb_0054DBC7[BB_0054DBC7]
  bb_0054DBCE[BB_0054DBCE]
  bb_0054DBB0 -->|branch| bb_0054DBBC
  bb_0054DBB0 -->|fallthrough| bb_0054DBB5
  bb_0054DBBB -->|flow| bb_0054DBBC
  bb_0054DBBC -->|branch| bb_0054DBC7
  bb_0054DBBC -->|fallthrough| bb_0054DBC0
  bb_0054DBC6 -->|flow| bb_0054DBC7
```
