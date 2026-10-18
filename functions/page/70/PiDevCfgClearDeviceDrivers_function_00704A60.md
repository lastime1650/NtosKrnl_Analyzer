# PiDevCfgClearDeviceDrivers

- RVA: `0x00704A60`–`0x00704AA3` (길이 `67` bytes)
- VA: `0x0000000140704A60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00704A8E` → [PiDevCfgFreeDriverNode](../73/PiDevCfgFreeDriverNode_function_00733354.md) (function, `0x00733354`)

### Direct callers
- [PiDevCfgFreeDeviceContext](PiDevCfgFreeDeviceContext_function_00704A00.md) at `0x00704A19`
- [PiDevCfgFindDeviceDriver](../97/PiDevCfgFindDeviceDriver_function_0097602C.md) at `0x009760CF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00704A60  40 53                           push rbx
00704A62  48 83 EC 20                     sub rsp, 0x20
00704A66  48 8D 59 18                     lea rbx, [rcx + 0x18]
00704A6A  48 83 3B 00                     cmp qword ptr [rbx], 0
00704A6E  74 2C                           je 0x140704a9c
00704A70  48 8B 0B                        mov rcx, qword ptr [rbx]
00704A73  48 3B CB                        cmp rcx, rbx
00704A76  74 24                           je 0x140704a9c
00704A78  48 39 59 08                     cmp qword ptr [rcx + 8], rbx
00704A7C  75 17                           jne 0x140704a95
00704A7E  48 8B 01                        mov rax, qword ptr [rcx]
00704A81  48 39 48 08                     cmp qword ptr [rax + 8], rcx
00704A85  75 0E                           jne 0x140704a95
00704A87  48 89 03                        mov qword ptr [rbx], rax
00704A8A  48 89 58 08                     mov qword ptr [rax + 8], rbx
00704A8E  E8 C1 E8 02 00                  call 0x140733354
00704A93  EB DB                           jmp 0x140704a70
00704A95  B9 03 00 00 00                  mov ecx, 3
00704A9A  CD 29                           int 0x29
00704A9C  48 83 C4 20                     add rsp, 0x20
00704AA0  5B                              pop rbx
00704AA1  C3                              ret
00704AA2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDevCfgClearDeviceDrivers(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if ((*(unsigned __int64 *)(a1 + 24)) == 0) goto loc_00704A9C;
loc_00704A70:
    if ((*(unsigned __int64 *)(a1 + 24)) == (a1 + 24)) goto loc_00704A9C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24) + 8)) != (a1 + 24)) goto loc_00704A95;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)) + 8)) != (*(unsigned __int64 *)(a1 + 24))) goto loc_00704A95;
    *(unsigned __int64 *)(a1 + 24) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24));
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 24)) + 8) = a1 + 24;
    result = PiDevCfgFreeDriverNode(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    goto loc_00704A70;
loc_00704A95:
loc_00704A9C:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDevCfgClearDeviceDrivers(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if ((*(uint64_t *)(arg1 + 0x18)) == 0) goto loc_00704A9C;
loc_00704A70:
    if ((*(uint64_t *)(arg1 + 0x18)) == (Arg1 + 24)) goto loc_00704A9C;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x18) + 0x8)) != (Arg1 + 24)) goto loc_00704A95;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)) + 0x8)) != (*(uint64_t *)(arg1 + 0x18))) goto loc_00704A95;
    *(uint64_t *)(arg1 + 0x18) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x18));
    *(void **)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x18)) + 0x8) = Arg1 + 24;
    result = PiDevCfgFreeDriverNode(*(uint64_t *)(arg1 + 0x18), a2, a3, a4);
    goto loc_00704A70;
loc_00704A95:
loc_00704A9C:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00704A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00704A60[BB_00704A60]
  bb_00704A70[BB_00704A70]
  bb_00704A78[BB_00704A78]
  bb_00704A7E[BB_00704A7E]
  bb_00704A87[BB_00704A87]
  bb_00704A95[BB_00704A95]
  bb_00704A9C[BB_00704A9C]
  bb_00704AA2[BB_00704AA2]
  bb_00704A60 -->|branch| bb_00704A9C
  bb_00704A60 -->|fallthrough| bb_00704A70
  bb_00704A70 -->|branch| bb_00704A9C
  bb_00704A70 -->|fallthrough| bb_00704A78
  bb_00704A78 -->|branch| bb_00704A95
  bb_00704A78 -->|fallthrough| bb_00704A7E
  bb_00704A7E -->|branch| bb_00704A95
  bb_00704A7E -->|fallthrough| bb_00704A87
  bb_00704A87 -->|branch| bb_00704A70
  bb_00704A95 -->|flow| bb_00704A9C
```
