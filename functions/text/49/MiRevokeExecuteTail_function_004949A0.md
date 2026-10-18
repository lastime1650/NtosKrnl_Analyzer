# MiRevokeExecuteTail

- RVA: `0x004949A0`–`0x004949D2` (길이 `50` bytes)
- VA: `0x00000001404949A0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A68`
- 디코드: `15`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004949BE` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x004949C3` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004949A0  40 53                           push rbx
004949A2  48 83 EC 20                     sub rsp, 0x20
004949A6  48 8B D9                        mov rbx, rcx
004949A9  48 8B 89 B8 00 00 00            mov rcx, qword ptr [rcx + 0xb8]
004949B0  48 85 C9                        test rcx, rcx
004949B3  75 09                           jne 0x1404949be
004949B5  33 C0                           xor eax, eax
004949B7  48 83 C4 20                     add rsp, 0x20
004949BB  5B                              pop rbx
004949BC  C3                              ret
004949BD  CC                              int3
004949BE  E8 FD D5 E7 FF                  call 0x140311fc0
004949C3  E8 A8 F2 E7 FF                  call 0x140313c70
004949C8  48 83 A3 B8 00 00 00 00         and qword ptr [rbx + 0xb8], 0
004949D0  EB E3                           jmp 0x1404949b5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRevokeExecuteTail(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 184) != 0) goto loc_004949BE;
loc_004949B5:
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_004949BE:
    result = MiFlushTbList(*(unsigned __int64 *)(a1 + 184), a2, a3, a4);
    result = MiReleaseProcessorFlushList(*(unsigned __int64 *)(a1 + 184), a2, a3, a4);
    goto loc_004949B5;
}
```

## 5. (Beta) C Style

```c
int64_t MiRevokeExecuteTail(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0xB8) != 0) goto loc_004949BE;
loc_004949B5:
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_004949BE:
    result = MiFlushTbList(*(uint64_t *)(arg1 + 0xB8), a2, a3, a4);
    result = MiReleaseProcessorFlushList(*(uint64_t *)(arg1 + 0xB8), a2, a3, a4);
    goto loc_004949B5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004949A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004949A0[BB_004949A0]
  bb_004949B5[BB_004949B5]
  bb_004949BD[BB_004949BD]
  bb_004949BE[BB_004949BE]
  bb_004949A0 -->|branch| bb_004949BE
  bb_004949A0 -->|fallthrough| bb_004949B5
  bb_004949BD -->|flow| bb_004949BE
  bb_004949BE -->|branch| bb_004949B5
```
