# PsSetThreadWin32Thread

- RVA: `0x00A3B0C0`–`0x00A3B0DF` (길이 `31` bytes)
- VA: `0x0000000140A3B0C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `31/31` bytes 표시
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
00A3B0C0  45 33 C9                        xor r9d, r9d
00A3B0C3  48 85 D2                        test rdx, rdx
00A3B0C6  75 0E                           jne 0x140a3b0d6
00A3B0C8  49 8B C0                        mov rax, r8
00A3B0CB  F0 4C 0F B1 89 C8 01 00 00      lock cmpxchg qword ptr [rcx + 0x1c8], r9
00A3B0D4  C3                              ret
00A3B0D5  CC                              int3
00A3B0D6  48 87 91 C8 01 00 00            xchg qword ptr [rcx + 0x1c8], rdx
00A3B0DD  C3                              ret
00A3B0DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSetThreadWin32Thread(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    a4 = 0;
    if (a2 != 0) goto loc_00A3B0D6;
    return a3;
loc_00A3B0D6:
    return a3;
}
```

## 5. (Beta) C Style

```c
int64_t PsSetThreadWin32Thread(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    Arg4 = 0;
    if (Arg2 != 0) goto loc_00A3B0D6;
    return Arg3;
loc_00A3B0D6:
    return Arg3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1C8` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A3B0C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A3B0C0[BB_00A3B0C0]
  bb_00A3B0C8[BB_00A3B0C8]
  bb_00A3B0D5[BB_00A3B0D5]
  bb_00A3B0D6[BB_00A3B0D6]
  bb_00A3B0DE[BB_00A3B0DE]
  bb_00A3B0C0 -->|branch| bb_00A3B0D6
  bb_00A3B0C0 -->|fallthrough| bb_00A3B0C8
  bb_00A3B0D5 -->|flow| bb_00A3B0D6
```
