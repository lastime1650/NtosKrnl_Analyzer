# ObQueryNameStringMode$fin$0

- RVA: `0x00B0EA90`–`0x00B0EAB6` (길이 `38` bytes)
- VA: `0x0000000140B0EA90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007F310`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0EAA2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B0EAA2` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0EA90  40 55                           push rbp
00B0EA92  48 83 EC 40                     sub rsp, 0x40
00B0EA96  48 8B EA                        mov rbp, rdx
00B0EA99  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00B0EA9D  48 85 C9                        test rcx, rcx
00B0EAA0  74 0D                           je 0x140b0eaaf
00B0EAA2  E8 A9 A8 7E FF                  call 0x1402f9350
00B0EAA7  48 C7 45 58 00 00 00 00         mov qword ptr [rbp + 0x58], 0
00B0EAAF  48 83 C4 40                     add rsp, 0x40
00B0EAB3  5D                              pop rbp
00B0EAB4  C3                              ret
00B0EAB5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObQueryNameStringMode_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    if (*(unsigned __int64 *)(a2 + 88) != 0) {
        result = ObfDereferenceObject(*(unsigned __int64 *)(a2 + 88), a2, a3, a4);
        *(unsigned __int64 *)(a2 + 88) = 0;
    }
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObQueryNameStringMode_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    if (*(uint64_t *)(arg2 + 0x58) != 0) {
        result = ObfDereferenceObject(*(uint64_t *)(arg2 + 0x58), Arg2, a3, a4);
        *(uint64_t *)(arg2 + 0x58) = 0;
    }
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0EA90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0EA90[BB_00B0EA90]
  bb_00B0EAA2[BB_00B0EAA2]
  bb_00B0EAAF[BB_00B0EAAF]
  bb_00B0EAB5[BB_00B0EAB5]
  bb_00B0EA90 -->|branch| bb_00B0EAAF
  bb_00B0EA90 -->|fallthrough| bb_00B0EAA2
  bb_00B0EAA2 -->|flow| bb_00B0EAAF
```
