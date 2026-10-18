# IoGetStackLimits

- RVA: `0x0041FD70`–`0x0041FD9D` (길이 `45` bytes)
- VA: `0x000000014041FD70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `16`개 명령, `45/45` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0041FD80` → [RtlpGetStackLimits](../2F/RtlpGetStackLimits_function_002F5F50.md) (function, `0x002F5F50`)

### Direct callers
- [EtwpTraceContextRegisters](../64/EtwpTraceContextRegisters_function_0064F108.md) at `0x0064F182`
- [RegRtlCopyTreeInternal](../../page/83/RegRtlCopyTreeInternal_function_008324C0.md) at `0x00832543`
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF3707`
- [HalpCheckLowMemoryPreSleep](../../pagelk/B5/HalpCheckLowMemoryPreSleep_function_00B5EB88.md) at `0x00B5EBC2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041FD70  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0041FD75  57                              push rdi
0041FD76  48 83 EC 20                     sub rsp, 0x20
0041FD7A  48 8B FA                        mov rdi, rdx
0041FD7D  48 8B D9                        mov rbx, rcx
0041FD80  E8 CB 61 ED FF                  call 0x1402f5f50
0041FD85  84 C0                           test al, al
0041FD87  75 08                           jne 0x14041fd91
0041FD89  33 C0                           xor eax, eax
0041FD8B  48 89 03                        mov qword ptr [rbx], rax
0041FD8E  48 89 07                        mov qword ptr [rdi], rax
0041FD91  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0041FD96  48 83 C4 20                     add rsp, 0x20
0041FD9A  5F                              pop rdi
0041FD9B  C3                              ret
0041FD9C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetStackLimits(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = RtlpGetStackLimits(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = 0;
        *(unsigned __int64 *)(a1) = 0;
        *(unsigned __int64 *)(a2) = 0;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetStackLimits(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = RtlpGetStackLimits(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) {
        result = 0;
        *(uint64_t *)(arg1) = 0;
        *(uint64_t *)(arg2) = 0;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041FD70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041FD70[BB_0041FD70]
  bb_0041FD89[BB_0041FD89]
  bb_0041FD91[BB_0041FD91]
  bb_0041FD9C[BB_0041FD9C]
  bb_0041FD70 -->|branch| bb_0041FD91
  bb_0041FD70 -->|fallthrough| bb_0041FD89
  bb_0041FD89 -->|flow| bb_0041FD91
```
