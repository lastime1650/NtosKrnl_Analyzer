# TtmpExitProximity

- RVA: `0x0077D438`–`0x0077D486` (길이 `78` bytes)
- VA: `0x000000014077D438`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0077D464` → [TtmiLogExitProximity](TtmiLogExitProximity_function_0077A258.md) (function, `0x0077A258`)
- `0x0077D475` → [TtmiScheduleSessionWorker](TtmiScheduleSessionWorker_function_00777184.md) (function, `0x00777184`)

### Direct callers
- [TtmiSetPendingOnOffRequest](TtmiSetPendingOnOffRequest_function_0077D074.md) at `0x0077D0BB`
- [TtmiTerminalMonitorControl](TtmiTerminalMonitorControl_function_0077D128.md) at `0x0077D1B7`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0077D438  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0077D43D  57                              push rdi
0077D43E  48 83 EC 20                     sub rsp, 0x20
0077D442  8B 42 24                        mov eax, dword ptr [rdx + 0x24]
0077D445  48 8B DA                        mov rbx, rdx
0077D448  48 8B F9                        mov rdi, rcx
0077D44B  A8 08                           test al, 8
0077D44D  74 2B                           je 0x14077d47a
0077D44F  8B 8B 0C 01 00 00               mov ecx, dword ptr [rbx + 0x10c]
0077D455  83 E0 F7                        and eax, 0xfffffff7
0077D458  83 C8 40                        or eax, 0x40
0077D45B  89 42 24                        mov dword ptr [rdx + 0x24], eax
0077D45E  8B 92 10 01 00 00               mov edx, dword ptr [rdx + 0x110]
0077D464  E8 EF CD FF FF                  call 0x14077a258
0077D469  83 4B 24 04                     or dword ptr [rbx + 0x24], 4
0077D46D  BA 02 00 00 00                  mov edx, 2
0077D472  48 8B CF                        mov rcx, rdi
0077D475  E8 0A 9D FF FF                  call 0x140777184
0077D47A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0077D47F  48 83 C4 20                     add rsp, 0x20
0077D483  5F                              pop rdi
0077D484  C3                              ret
0077D485  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall TtmpExitProximity(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(*(unsigned int *)(a2 + 36));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 36)))) & (8)) != 0) {
        a1 = *(unsigned int *)(a2 + 268);
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 36))) & (0xFFFFFFF7ULL));
        result = (unsigned int)((result) | (64));
        *(unsigned int *)(a2 + 36) = (unsigned int)(result);
        a2 = *(unsigned int *)(a2 + 272);
        result = TtmiLogExitProximity(a1, a2, a3, a4);
        a2 = 2;
        a1 = a1;
        result = TtmiScheduleSessionWorker(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t TtmpExitProximity(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x24));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x24)))) & (8)) != 0) {
        Arg1 = *(uint32_t *)(arg2 + 0x10C);
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x24))) & (0xFFFFFFF7ULL));
        result = (uint32_t)((result) | (64));
        *(uint32_t *)(arg2 + 0x24) = (uint32_t)(result);
        Arg2 = *(uint32_t *)(arg2 + 0x110);
        result = TtmiLogExitProximity(Arg1, Arg2, a3, a4);
        Arg2 = 2;
        Arg1 = Arg1;
        result = TtmiScheduleSessionWorker(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x24` | `32` | `R` |
| `Arg2` | `+ 0x24` | `32` | `R/W` |
| `Arg2` | `+ 0x24` | `32` | `W` |
| `Arg2` | `+ 0x10C` | `32` | `R` |
| `Arg2` | `+ 0x110` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0077D438&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0077D438[BB_0077D438]
  bb_0077D44F[BB_0077D44F]
  bb_0077D47A[BB_0077D47A]
  bb_0077D485[BB_0077D485]
  bb_0077D438 -->|branch| bb_0077D47A
  bb_0077D438 -->|fallthrough| bb_0077D44F
  bb_0077D44F -->|flow| bb_0077D47A
```
