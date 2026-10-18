# EtwpCheckSystemTraceAccess

- RVA: `0x00A8DE44`–`0x00A8DE77` (길이 `51` bytes)
- VA: `0x0000000140A8DE44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A88`
- 디코드: `15`개 명령, `51/51` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A8DE5F` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x00A8DE70` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)

### Direct callers
- [EtwpUpdateTrace](../AB/EtwpUpdateTrace_function_00ABCC7C.md) at `0x00ABCF66`
- [EtwQueryPerformanceTraceInformation](../AF/EtwQueryPerformanceTraceInformation_function_00AF28A4.md) at `0x00AF2DE9`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3CC1A`
- [sub_00B3C988](../B3/Unknown_function_00B3C988.md) at `0x00B3CEC0`

### Static image references
- `0x00A8DE58` → RVA `0x00011F40` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8DE44  48 83 EC 28                     sub rsp, 0x28
00A8DE48  8B 81 30 03 00 00               mov eax, dword ptr [rcx + 0x330]
00A8DE4E  44 8B CA                        mov r9d, edx
00A8DE51  A8 20                           test al, 0x20
00A8DE53  75 15                           jne 0x140a8de6a
00A8DE55  45 33 C0                        xor r8d, r8d
00A8DE58  48 8D 0D E1 40 58 FF            lea rcx, [rip - 0xa7bf1f]
00A8DE5F  E8 18 8B E3 FF                  call 0x1408c697c
00A8DE64  48 83 C4 28                     add rsp, 0x28
00A8DE68  C3                              ret
00A8DE69  CC                              int3
00A8DE6A  48 8B D1                        mov rdx, rcx
00A8DE6D  41 8B C9                        mov ecx, r9d
00A8DE70  E8 6B 2C E3 FF                  call 0x1408c0ae0
00A8DE75  EB ED                           jmp 0x140a8de64
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCheckSystemTraceAccess(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 816)))) & (32)) != 0) goto loc_00A8DE6A;
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 10993439, a2, a3, (unsigned int)(a2));
loc_00A8DE64:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A8DE6A:
    result = EtwpCheckLoggerControlAccess((unsigned int)((unsigned int)((unsigned int)(a2))), v_rip - 10993439, a3, (unsigned int)(a2));
    goto loc_00A8DE64;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCheckSystemTraceAccess(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x330)))) & (32)) != 0) goto loc_00A8DE6A;
    Arg3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 10993439, Arg2, Arg3, (uint32_t)(Arg2));
loc_00A8DE64:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A8DE6A:
    result = EtwpCheckLoggerControlAccess((uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip - 10993439, Arg3, (uint32_t)(Arg2));
    goto loc_00A8DE64;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x330` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8DE44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8DE44[BB_00A8DE44]
  bb_00A8DE55[BB_00A8DE55]
  bb_00A8DE64[BB_00A8DE64]
  bb_00A8DE69[BB_00A8DE69]
  bb_00A8DE6A[BB_00A8DE6A]
  bb_00A8DE44 -->|branch| bb_00A8DE6A
  bb_00A8DE44 -->|fallthrough| bb_00A8DE55
  bb_00A8DE55 -->|flow| bb_00A8DE64
  bb_00A8DE69 -->|flow| bb_00A8DE6A
  bb_00A8DE6A -->|branch| bb_00A8DE64
```
