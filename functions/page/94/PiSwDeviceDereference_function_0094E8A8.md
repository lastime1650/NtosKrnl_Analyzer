# PiSwDeviceDereference

- RVA: `0x0094E8A8`–`0x0094E8D8` (길이 `48` bytes)
- VA: `0x000000014094E8A8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060A68`
- 디코드: `16`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0094E8C4` → [PiSwDeviceFree](../8D/PiSwDeviceFree_function_008DA63C.md) (function, `0x008DA63C`)
- `0x0094E8D1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiSwDispatch](../73/PiSwDispatch_function_0073AA90.md) at `0x0073AB94`
- [PiSwIrpStartCreateWorker](../8D/PiSwIrpStartCreateWorker_function_008DB398.md) at `0x008DB8C5`
- [PiSwIrpStartCreateWorker](../8D/PiSwIrpStartCreateWorker_function_008DB398.md) at `0x008DB8CF`
- [PiSwBusRelationRemove](PiSwBusRelationRemove_function_0094D9C0.md) at `0x0094DA68`
- [PiSwProcessRemove](PiSwProcessRemove_function_0094E3B8.md) at `0x0094E603`
- [PiSwUnassociateDeviceObject](PiSwUnassociateDeviceObject_function_0094E868.md) at `0x0094E88C`
- [sub_00B1C4F6](../B1/Unknown_function_00B1C4F6.md) at `0x00B1C867`
- [sub_00B4A56C](../B4/Unknown_function_00B4A56C.md) at `0x00B4A5A4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0094E8D1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0094E8A8  40 53                           push rbx
0094E8AA  48 83 EC 20                     sub rsp, 0x20
0094E8AE  48 8B D9                        mov rbx, rcx
0094E8B1  83 C8 FF                        or eax, 0xffffffff
0094E8B4  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
0094E8B8  83 F8 01                        cmp eax, 1
0094E8BB  74 07                           je 0x14094e8c4
0094E8BD  48 83 C4 20                     add rsp, 0x20
0094E8C1  5B                              pop rbx
0094E8C2  C3                              ret
0094E8C3  CC                              int3
0094E8C4  E8 73 BD F8 FF                  call 0x1408da63c
0094E8C9  BA 50 6E 70 57                  mov edx, 0x57706e50
0094E8CE  48 8B CB                        mov rcx, rbx
0094E8D1  E8 9A 3F 23 00                  call 0x140b82870
0094E8D6  EB E5                           jmp 0x14094e8bd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwDeviceDereference(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    if (((unsigned int)(result)) == 1) goto loc_0094E8C4;
loc_0094E8BD:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0094E8C4:
    result = PiSwDeviceFree(a1, a2, a3, a4);
    result = ExFreePoolWithTag(a1, (unsigned int)(0x57706E50ULL), a3, a4);
    goto loc_0094E8BD;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwDeviceDereference(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    if (((uint32_t)(result)) == 1) goto loc_0094E8C4;
loc_0094E8BD:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0094E8C4:
    result = PiSwDeviceFree(Arg1, a2, a3, a4);
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x57706E50ULL), a3, a4);
    goto loc_0094E8BD;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0094E8A8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0094E8A8[BB_0094E8A8]
  bb_0094E8BD[BB_0094E8BD]
  bb_0094E8C3[BB_0094E8C3]
  bb_0094E8C4[BB_0094E8C4]
  bb_0094E8A8 -->|branch| bb_0094E8C4
  bb_0094E8A8 -->|fallthrough| bb_0094E8BD
  bb_0094E8C3 -->|flow| bb_0094E8C4
  bb_0094E8C4 -->|branch| bb_0094E8BD
```
