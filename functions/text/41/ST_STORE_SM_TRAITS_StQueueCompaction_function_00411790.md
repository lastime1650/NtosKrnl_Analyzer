# ST_STORE&lt;SM_TRAITS&gt;::StQueueCompaction

- RVA: `0x00411790`–`0x004117F8` (길이 `104` bytes)
- VA: `0x0000000140411790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076838`
- 디코드: `27`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004117C9` → [ST_STORE<SM_TRAITS>::StLazyWorkMgrQueueWork](ST_STORE_SM_TRAITS_StLazyWorkMgrQueueWork_function_00411800.md) (function, `0x00411800`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StDmPageRemove](../20/ST_STORE_SM_TRAITS_StDmPageRemove_function_002049A0.md) at `0x00204ED0`
- [sub_002061A0](../20/Unknown_function_002061A0.md) at `0x002062FB`
- [ST_STORE&lt;SM_TRAITS&gt;::StCompactionWorker](ST_STORE_SM_TRAITS_StCompactionWorker_function_00411118.md) at `0x0041119D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00411790  48 83 EC 28                     sub rsp, 0x28
00411794  44 8B 91 40 03 00 00            mov r10d, dword ptr [rcx + 0x340]
0041179B  41 D1 EA                        shr r10d, 1
0041179E  41 83 E2 01                     and r10d, 1
004117A2  83 FA 01                        cmp edx, 1
004117A5  8A 91 E8 08 00 00               mov dl, byte ptr [rcx + 0x8e8]
004117AB  74 27                           je 0x1404117d4
004117AD  45 33 C9                        xor r9d, r9d
004117B0  80 E2 FE                        and dl, 0xfe
004117B3  45 8B C1                        mov r8d, r9d
004117B6  80 CA 02                        or dl, 2
004117B9  88 91 E8 08 00 00               mov byte ptr [rcx + 0x8e8], dl
004117BF  41 8B D2                        mov edx, r10d
004117C2  48 8B 89 F0 08 00 00            mov rcx, qword ptr [rcx + 0x8f0]
004117C9  E8 32 00 00 00                  call 0x140411800
004117CE  48 83 C4 28                     add rsp, 0x28
004117D2  C3                              ret
004117D3  CC                              int3
004117D4  8B 81 08 03 00 00               mov eax, dword ptr [rcx + 0x308]
004117DA  80 E2 FD                        and dl, 0xfd
004117DD  80 CA 01                        or dl, 1
004117E0  41 B9 FE FF FF FF               mov r9d, 0xfffffffe
004117E6  F6 D8                           neg al
004117E8  45 1B C0                        sbb r8d, r8d
004117EB  41 81 E0 72 01 00 00            and r8d, 0x172
004117F2  41 83 C0 1E                     add r8d, 0x1e
004117F6  EB C1                           jmp 0x1404117b9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StQueueCompaction(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 832))) >> (1));
    v_r10 = (unsigned int)((v_r10) & (1));
    if (a2 == 1) goto loc_004117D4;
    a4 = 0;
    a2 = (unsigned __int8)((*(unsigned __int8 *)(a1 + 2280)) & (254));
    a2 = (unsigned __int8)((a2) | (2));
loc_004117B9:
    *(unsigned __int8 *)(a1 + 2280) = (unsigned __int8)(a2);
    result = ST_STORE_SM_TRAITS___StLazyWorkMgrQueueWork(*(unsigned __int64 *)(a1 + 2288), (unsigned int)((unsigned int)(v_r10)), 0, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_004117D4:
    a2 = (unsigned __int8)(((unsigned int)((unsigned int)(v_r10))) & (253));
    a2 = (unsigned __int8)((a2) | (1));
    result = (unsigned __int8)(-((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 2288) + 776))));
    a3 = (unsigned int)((0) & (370));
    a3 = (unsigned int)((a3) + (30));
    goto loc_004117B9;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StQueueCompaction(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x340))) >> (1));
    local_r10 = (uint32_t)((local_r10) & (1));
    if (Arg2 == 1) goto loc_004117D4;
    Arg4 = 0;
    Arg2 = (uint8_t)((*(uint8_t *)(arg1 + 0x8E8)) & (254));
    Arg2 = (uint8_t)((Arg2) | (2));
loc_004117B9:
    *(uint8_t *)(arg1 + 0x8E8) = (uint8_t)(Arg2);
    result = ST_STORE_SM_TRAITS___StLazyWorkMgrQueueWork(*(uint64_t *)(arg1 + 0x8F0), (uint32_t)((uint32_t)(local_r10)), 0, Arg4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_004117D4:
    Arg2 = (uint8_t)(((uint32_t)((uint32_t)(local_r10))) & (253));
    Arg2 = (uint8_t)((Arg2) | (1));
    result = (uint8_t)(-((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8F0) + 0x308))));
    Arg3 = (uint32_t)((0) & (370));
    Arg3 = (uint32_t)((Arg3) + (30));
    goto loc_004117B9;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x308` | `32` | `R` |
| `Arg1` | `+ 0x340` | `32` | `R` |
| `Arg1` | `+ 0x8E8` | `8` | `R` |
| `Arg1` | `+ 0x8E8` | `8` | `W` |
| `Arg1` | `+ 0x8F0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00411790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00411790[BB_00411790]
  bb_004117AD[BB_004117AD]
  bb_004117B9[BB_004117B9]
  bb_004117D3[BB_004117D3]
  bb_004117D4[BB_004117D4]
  bb_00411790 -->|branch| bb_004117D4
  bb_00411790 -->|fallthrough| bb_004117AD
  bb_004117AD -->|flow| bb_004117B9
  bb_004117D3 -->|flow| bb_004117D4
  bb_004117D4 -->|branch| bb_004117B9
```
