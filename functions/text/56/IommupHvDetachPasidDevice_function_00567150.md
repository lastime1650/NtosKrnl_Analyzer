# IommupHvDetachPasidDevice

- RVA: `0x00567150`–`0x005671AD` (길이 `93` bytes)
- VA: `0x0000000140567150`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0056716D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00567183` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00567192` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005671A1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [IommupDeviceDisableSvm](../../page/70/IommupDeviceDisableSvm_function_00708A28.md) at `0x00708ABB`
- [IommupDeviceEnableSvm](../../page/70/IommupDeviceEnableSvm_function_00708CC4.md) at `0x00708E80`

### Static image references
- `0x00567163` → RVA `0x00FC1D88` (`.data`; read)
- `0x00567172` → RVA `0x00FC1DC8` (`.data`; read)
- `0x00567188` → RVA `0x00FC1E18` (`.data`; read)
- `0x00567197` → RVA `0x00FC1EC0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00567150  40 53                           push rbx
00567152  48 83 EC 20                     sub rsp, 0x20
00567156  80 B9 11 01 00 00 00            cmp byte ptr [rcx + 0x111], 0
0056715D  48 8D 59 20                     lea rbx, [rcx + 0x20]
00567161  74 25                           je 0x140567188
00567163  48 8B 05 1E AC A5 00            mov rax, qword ptr [rip + 0xa5ac1e]
0056716A  48 8B 0B                        mov rcx, qword ptr [rbx]
0056716D  E8 5E 39 15 00                  call 0x1406baad0
00567172  48 8B 05 4F AC A5 00            mov rax, qword ptr [rip + 0xa5ac4f]
00567179  45 33 C0                        xor r8d, r8d
0056717C  48 8B 0B                        mov rcx, qword ptr [rbx]
0056717F  41 8D 50 21                     lea edx, [r8 + 0x21]
00567183  E8 48 39 15 00                  call 0x1406baad0
00567188  48 8B 05 89 AC A5 00            mov rax, qword ptr [rip + 0xa5ac89]
0056718F  48 8B 0B                        mov rcx, qword ptr [rbx]
00567192  E8 39 39 15 00                  call 0x1406baad0
00567197  48 8B 05 22 AD A5 00            mov rax, qword ptr [rip + 0xa5ad22]
0056719E  48 8B 0B                        mov rcx, qword ptr [rbx]
005671A1  E8 2A 39 15 00                  call 0x1406baad0
005671A6  48 83 C4 20                     add rsp, 0x20
005671AA  5B                              pop rbx
005671AB  C3                              ret
005671AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IommupHvDetachPasidDevice(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int8 *)(a1 + 273)) != 0) {
        result = *(unsigned __int64 *)(v_rip + 10857502);
        a1 = *(unsigned __int64 *)(a1 + 32);
        result = guard_dispatch_icall(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rip + 10857551);
        a3 = 0;
        a1 = *(unsigned __int64 *)(a1 + 32);
        a2 = a3 + 33;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    result = guard_dispatch_icall(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IommupHvDetachPasidDevice(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint8_t *)(arg1 + 0x111)) != 0) {
        result = *(uint64_t *)(v_rip + 0xA5AC1E);
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
        result = *(uint64_t *)(v_rip + 0xA5AC4F);
        Arg3 = 0;
        Arg1 = *(uint64_t *)(arg1 + 0x20);
        Arg2 = Arg3 + 33;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x20), Arg2, Arg3, a4);
    result = guard_dispatch_icall(*(uint64_t *)(arg1 + 0x20), Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x111` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00567150&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00567150[BB_00567150]
  bb_00567163[BB_00567163]
  bb_00567188[BB_00567188]
  bb_005671AC[BB_005671AC]
  bb_00567150 -->|branch| bb_00567188
  bb_00567150 -->|fallthrough| bb_00567163
  bb_00567163 -->|flow| bb_00567188
```
