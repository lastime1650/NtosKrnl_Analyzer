# EtwpLogFileNameRundown

- RVA: `0x007C00F0`–`0x007C013E` (길이 `78` bytes)
- VA: `0x00000001407C00F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `24`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007C0113` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x007C0123` → [WmiTraceRundownNotify](../9E/WmiTraceRundownNotify_function_009E46E0.md) (function, `0x009E46E0`)

### Direct callers
- [EtwpEnableDisableSpecialGuids](../9E/EtwpEnableDisableSpecialGuids_function_009E3A88.md) at `0x009E3C74`

### Static image references
- `0x007C0109` → RVA `0x00022BF0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C00F0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007C00F5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007C00FA  57                              push rdi
007C00FB  48 83 EC 20                     sub rsp, 0x20
007C00FF  8B DA                           mov ebx, edx
007C0101  48 8B F9                        mov rdi, rcx
007C0104  BA 80 00 00 00                  mov edx, 0x80
007C0109  48 8D 0D E0 2A 86 FF            lea rcx, [rip - 0x79d520]
007C0110  45 33 C0                        xor r8d, r8d
007C0113  E8 64 68 10 00                  call 0x1408c697c
007C0118  33 F6                           xor esi, esi
007C011A  85 C0                           test eax, eax
007C011C  78 0F                           js 0x1407c012d
007C011E  48 8B 0F                        mov rcx, qword ptr [rdi]
007C0121  8B D3                           mov edx, ebx
007C0123  E8 B8 45 22 00                  call 0x1409e46e0
007C0128  85 C0                           test eax, eax
007C012A  0F 49 C6                        cmovns eax, esi
007C012D  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
007C0132  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007C0137  48 83 C4 20                     add rsp, 0x20
007C013B  5F                              pop rdi
007C013C  C3                              ret
007C013D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpLogFileNameRundown(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 7984416, 128, a3, a4);
    v_rsi = 0;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1);
        a2 = (unsigned int)((unsigned int)(a2));
        result = WmiTraceRundownNotify(a1, a2, a3, a4);
        if (!sign_flag) { result = 0; }
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpLogFileNameRundown(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 7984416, 128, Arg3, a4);
    local_rsi = 0;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1);
        Arg2 = (uint32_t)((uint32_t)(Arg2));
        result = WmiTraceRundownNotify(Arg1, Arg2, Arg3, a4);
        if (!sign_flag) { result = 0; }
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C00F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C00F0[BB_007C00F0]
  bb_007C011E[BB_007C011E]
  bb_007C012D[BB_007C012D]
  bb_007C013D[BB_007C013D]
  bb_007C00F0 -->|branch| bb_007C012D
  bb_007C00F0 -->|fallthrough| bb_007C011E
  bb_007C011E -->|flow| bb_007C012D
```
