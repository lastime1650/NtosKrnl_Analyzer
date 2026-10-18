# EtwpRelinquishCompressionTarget

- RVA: `0x00653818`–`0x0065385F` (길이 `71` bytes)
- VA: `0x0000000140653818`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0065382B` → [EtwpGetLoggerTimeStamp](../37/EtwpGetLoggerTimeStamp_function_0037E690.md) (function, `0x0037E690`)
- `0x0065384B` → [EtwpEnqueueAvailableBuffer](../2F/EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (function, `0x002FE7DC`)

### Direct callers
- [EtwpBufferingModeCompressionFlush](EtwpBufferingModeCompressionFlush_function_00652D24.md) at `0x00652D7E`
- [EtwpCompressionProc](EtwpCompressionProc_function_00653300.md) at `0x0065338A`
- [EtwpDisableCompression](EtwpDisableCompression_function_006534F8.md) at `0x0065356B`
- [sub_006F31F0](../6F/Unknown_function_006F31F0.md) at `0x006F31FC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00653818  40 53                           push rbx
0065381A  48 83 EC 20                     sub rsp, 0x20
0065381E  48 83 B9 88 05 00 00 00         cmp qword ptr [rcx + 0x588], 0
00653826  48 8B D9                        mov rbx, rcx
00653829  74 2D                           je 0x140653858
0065382B  E8 60 AE D2 FF                  call 0x14037e690
00653830  48 8B 93 88 05 00 00            mov rdx, qword ptr [rbx + 0x588]
00653837  41 B8 05 00 00 00               mov r8d, 5
0065383D  48 8B CB                        mov rcx, rbx
00653840  48 89 42 10                     mov qword ptr [rdx + 0x10], rax
00653844  48 8B 93 88 05 00 00            mov rdx, qword ptr [rbx + 0x588]
0065384B  E8 8C AF CA FF                  call 0x1402fe7dc
00653850  48 83 A3 88 05 00 00 00         and qword ptr [rbx + 0x588], 0
00653858  48 83 C4 20                     add rsp, 0x20
0065385C  5B                              pop rbx
0065385D  C3                              ret
0065385E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpRelinquishCompressionTarget(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(a1 + 1416)) != 0) {
        result = EtwpGetLoggerTimeStamp(a1, a2, a3, a4);
        a2 = *(unsigned __int64 *)(a1 + 1416);
        a3 = 5;
        a1 = a1;
        *(unsigned __int64 *)(a2 + 16) = result;
        a2 = *(unsigned __int64 *)(a1 + 1416);
        result = EtwpEnqueueAvailableBuffer(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpRelinquishCompressionTarget(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(arg1 + 0x588)) != 0) {
        result = EtwpGetLoggerTimeStamp(Arg1, a2, a3, a4);
        a2 = *(uint64_t *)(arg1 + 0x588);
        a3 = 5;
        Arg1 = Arg1;
        *(uint64_t *)(a2 + 0x10) = result;
        a2 = *(uint64_t *)(arg1 + 0x588);
        result = EtwpEnqueueAvailableBuffer(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x588` | `64` | `R` |
| `Arg1` | `+ 0x588` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00653818&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00653818[BB_00653818]
  bb_0065382B[BB_0065382B]
  bb_00653858[BB_00653858]
  bb_0065385E[BB_0065385E]
  bb_00653818 -->|branch| bb_00653858
  bb_00653818 -->|fallthrough| bb_0065382B
  bb_0065382B -->|flow| bb_00653858
```
