# PspFindPropertySetEntry

- RVA: `0x00434CD0`–`0x00434CE7` (길이 `23` bytes)
- VA: `0x0000000140434CD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspInsertProperty](PspInsertProperty_function_00434B2C.md) at `0x00434B7F`
- [PspRemoveProperty](PspRemoveProperty_function_00434C10.md) at `0x00434C3F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00434CD0  48 8B 01                        mov rax, qword ptr [rcx]
00434CD3  48 3B C1                        cmp rax, rcx
00434CD6  75 04                           jne 0x140434cdc
00434CD8  33 C0                           xor eax, eax
00434CDA  C3                              ret
00434CDB  CC                              int3
00434CDC  48 39 50 10                     cmp qword ptr [rax + 0x10], rdx
00434CE0  74 F8                           je 0x140434cda
00434CE2  48 8B 00                        mov rax, qword ptr [rax]
00434CE5  EB EC                           jmp 0x140434cd3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspFindPropertySetEntry(__int64 a1, __int64 a2)
{
    __int64 result;

loc_00434CD3:
    if ((*(unsigned __int64 *)(a1)) != a1) goto loc_00434CDC;
    result = 0;
loc_00434CDA:
    return result;
loc_00434CDC:
    if ((*(unsigned __int64 *)(result + 16)) == a2) goto loc_00434CDA;
    goto loc_00434CD3;
}
```

## 5. (Beta) C Style

```c
int64_t PspFindPropertySetEntry(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

loc_00434CD3:
    if ((*(uint64_t *)(arg1)) != Arg1) goto loc_00434CDC;
    result = 0;
loc_00434CDA:
    return result;
loc_00434CDC:
    if ((*(uint64_t *)(result + 0x10)) == Arg2) goto loc_00434CDA;
    goto loc_00434CD3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00434CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00434CD0[BB_00434CD0]
  bb_00434CD3[BB_00434CD3]
  bb_00434CD8[BB_00434CD8]
  bb_00434CDA[BB_00434CDA]
  bb_00434CDB[BB_00434CDB]
  bb_00434CDC[BB_00434CDC]
  bb_00434CE2[BB_00434CE2]
  bb_00434CD0 -->|flow| bb_00434CD3
  bb_00434CD3 -->|branch| bb_00434CDC
  bb_00434CD3 -->|fallthrough| bb_00434CD8
  bb_00434CD8 -->|flow| bb_00434CDA
  bb_00434CDB -->|flow| bb_00434CDC
  bb_00434CDC -->|branch| bb_00434CDA
  bb_00434CDC -->|fallthrough| bb_00434CE2
  bb_00434CE2 -->|branch| bb_00434CD3
```
