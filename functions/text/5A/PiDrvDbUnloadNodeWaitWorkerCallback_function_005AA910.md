# PiDrvDbUnloadNodeWaitWorkerCallback

- RVA: `0x005AA910`–`0x005AA9A6` (길이 `150` bytes)
- VA: `0x00000001405AA910`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `36`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005AA92E` → [ZwWaitForSingleObject](../6A/ZwWaitForSingleObject_function_006AD150.md) (function, `0x006AD150`)
- `0x005AA94C` → [ExAcquireResourceExclusiveLite](../21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x005AA96F` → [PnpDiagnosticTraceObjectWithStatus](../4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (function, `0x004A9F58`)
- `0x005AA982` → [PnpDiagnosticTraceObjectWithStatus](../4A/PnpDiagnosticTraceObjectWithStatus_function_004A9F58.md) (function, `0x004A9F58`)
- `0x005AA98B` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x005AA990` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005AA968` → RVA `0x00026D90` (`.rdata`; read)
- `0x005AA97B` → RVA `0x00027738` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005AA910  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005AA915  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005AA91A  57                              push rdi
005AA91B  48 83 EC 20                     sub rsp, 0x20
005AA91F  48 8B D9                        mov rbx, rcx
005AA922  45 33 C0                        xor r8d, r8d
005AA925  48 8B 89 D8 01 00 00            mov rcx, qword ptr [rcx + 0x1d8]
005AA92C  33 D2                           xor edx, edx
005AA92E  E8 1D 28 10 00                  call 0x1406ad150
005AA933  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
005AA93C  48 8D 4B 58                     lea rcx, [rbx + 0x58]
005AA940  8B F0                           mov esi, eax
005AA942  66 FF 8A E4 01 00 00            dec word ptr [rdx + 0x1e4]
005AA949  B2 01                           mov dl, 1
005AA94B  90                              nop
005AA94C  E8 CF A4 C6 FF                  call 0x140214e20
005AA951  80 BB E9 01 00 00 00            cmp byte ptr [rbx + 0x1e9], 0
005AA958  75 2D                           jne 0x1405aa987
005AA95A  44 8B C6                        mov r8d, esi
005AA95D  C6 83 E9 01 00 00 01            mov byte ptr [rbx + 0x1e9], 1
005AA964  48 8D 53 10                     lea rdx, [rbx + 0x10]
005AA968  48 8D 0D 21 C4 A7 FF            lea rcx, [rip - 0x583bdf]
005AA96F  E8 E4 F5 EF FF                  call 0x1404a9f58
005AA974  44 8B C6                        mov r8d, esi
005AA977  48 8D 53 10                     lea rdx, [rbx + 0x10]
005AA97B  48 8D 0D B6 CD A7 FF            lea rcx, [rip - 0x58324a]
005AA982  E8 D1 F5 EF FF                  call 0x1404a9f58
005AA987  48 8D 4B 58                     lea rcx, [rbx + 0x58]
005AA98B  E8 80 50 CB FF                  call 0x14025fa10
005AA990  E8 1B 2F CB FF                  call 0x14025d8b0
005AA995  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
005AA99A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
005AA99F  48 83 C4 20                     add rsp, 0x20
005AA9A3  5F                              pop rdi
005AA9A4  C3                              ret
005AA9A5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDrvDbUnloadNodeWaitWorkerCallback(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = ZwWaitForSingleObject(*(unsigned __int64 *)(a1 + 472), a2, a3, a4);
    result = ExAcquireResourceExclusiveLite(a1 + 88, 1, a3, a4);
    if ((*(unsigned __int8 *)(a1 + 489)) == 0) {
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int8 *)(a1 + 489) = 1;
        a2 = a1 + 16;
        a1 = v_rip - 5782495;
        result = PnpDiagnosticTraceObjectWithStatus(a1, a2, a3, a4);
        a3 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a2 = a1 + 16;
        a1 = v_rip - 5780042;
        result = PnpDiagnosticTraceObjectWithStatus(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(a1 + 88, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 88, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDrvDbUnloadNodeWaitWorkerCallback(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = ZwWaitForSingleObject(*(uint64_t *)(arg1 + 0x1D8), Arg2, Arg3, a4);
    result = ExAcquireResourceExclusiveLite(Arg1 + 88, 1, Arg3, a4);
    if ((*(uint8_t *)(arg1 + 0x1E9)) == 0) {
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint8_t *)(arg1 + 0x1E9) = 1;
        Arg2 = Arg1 + 16;
        Arg1 = v_rip - 5782495;
        result = PnpDiagnosticTraceObjectWithStatus(Arg1, Arg2, Arg3, a4);
        Arg3 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg2 = Arg1 + 16;
        Arg1 = v_rip - 5780042;
        result = PnpDiagnosticTraceObjectWithStatus(Arg1, Arg2, Arg3, a4);
    }
    result = ExReleaseResourceLite(Arg1 + 88, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 88, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R` |
| `Arg1` | `+ 0x1D8` | `64` | `R` |
| `Arg1` | `+ 0x1E9` | `8` | `R` |
| `Arg1` | `+ 0x1E9` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005AA910&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005AA910[BB_005AA910]
  bb_005AA95A[BB_005AA95A]
  bb_005AA987[BB_005AA987]
  bb_005AA9A5[BB_005AA9A5]
  bb_005AA910 -->|branch| bb_005AA987
  bb_005AA910 -->|fallthrough| bb_005AA95A
  bb_005AA95A -->|flow| bb_005AA987
```
