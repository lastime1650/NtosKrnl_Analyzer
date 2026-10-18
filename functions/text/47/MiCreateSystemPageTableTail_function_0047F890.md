# MiCreateSystemPageTableTail

- RVA: `0x0047F890`–`0x0047F8C6` (길이 `54` bytes)
- VA: `0x000000014047F890`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A68`
- 디코드: `15`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0047F8B2` → [MiFlushTbList](../31/MiFlushTbList_function_00311FC0.md) (function, `0x00311FC0`)
- `0x0047F8B7` → [MiReleaseProcessorFlushList](../31/MiReleaseProcessorFlushList_function_00313C70.md) (function, `0x00313C70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047F890  40 53                           push rbx
0047F892  48 83 EC 20                     sub rsp, 0x20
0047F896  48 8B 99 B8 00 00 00            mov rbx, qword ptr [rcx + 0xb8]
0047F89D  48 8B 8B 88 00 00 00            mov rcx, qword ptr [rbx + 0x88]
0047F8A4  48 85 C9                        test rcx, rcx
0047F8A7  75 09                           jne 0x14047f8b2
0047F8A9  33 C0                           xor eax, eax
0047F8AB  48 83 C4 20                     add rsp, 0x20
0047F8AF  5B                              pop rbx
0047F8B0  C3                              ret
0047F8B1  CC                              int3
0047F8B2  E8 09 27 E9 FF                  call 0x140311fc0
0047F8B7  E8 B4 43 E9 FF                  call 0x140313c70
0047F8BC  48 83 A3 88 00 00 00 00         and qword ptr [rbx + 0x88], 0
0047F8C4  EB E3                           jmp 0x14047f8a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreateSystemPageTableTail(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 136) != 0) goto loc_0047F8B2;
loc_0047F8A9:
    result = 0;
    v_rsp = (v_rsp) + (32);
    return result;
loc_0047F8B2:
    result = MiFlushTbList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 136), a2, a3, a4);
    result = MiReleaseProcessorFlushList(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 184) + 136), a2, a3, a4);
    goto loc_0047F8A9;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreateSystemPageTableTail(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x88) != 0) goto loc_0047F8B2;
loc_0047F8A9:
    result = 0;
    local_rsp = (local_rsp) + (32);
    return result;
loc_0047F8B2:
    result = MiFlushTbList(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x88), a2, a3, a4);
    result = MiReleaseProcessorFlushList(*(uint64_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x88), a2, a3, a4);
    goto loc_0047F8A9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047F890&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047F890[BB_0047F890]
  bb_0047F8A9[BB_0047F8A9]
  bb_0047F8B1[BB_0047F8B1]
  bb_0047F8B2[BB_0047F8B2]
  bb_0047F890 -->|branch| bb_0047F8B2
  bb_0047F890 -->|fallthrough| bb_0047F8A9
  bb_0047F8B1 -->|flow| bb_0047F8B2
  bb_0047F8B2 -->|branch| bb_0047F8A9
```
