# PopRecordBatteryPercentage

- RVA: `0x00AC5EB4`–`0x00AC5EF8` (길이 `68` bytes)
- VA: `0x0000000140AC5EB4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00AC5EC3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AC5EE0` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x00AC5EEC` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopBatteryApplyCompositeState](../AE/PopBatteryApplyCompositeState_function_00AE0CD0.md) at `0x00AE0E89`

### Static image references
- `0x00AC5EBC` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00AC5EC8` → RVA `0x00E6741F` (`.data`; read)
- `0x00AC5EDA` → RVA `0x00E6741F` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AC5EC3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AC5EE0` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x00AC5EEC` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC5EB4  40 53                           push rbx
00AC5EB6  48 83 EC 20                     sub rsp, 0x20
00AC5EBA  8B D9                           mov ebx, ecx
00AC5EBC  48 8D 0D 1D 93 44 00            lea rcx, [rip + 0x44931d]
00AC5EC3  E8 7C AC 96 FF                  call 0x140430b44
00AC5EC8  8A 05 51 15 3A 00               mov al, byte ptr [rip + 0x3a1551]
00AC5ECE  80 E3 7F                        and bl, 0x7f
00AC5ED1  24 80                           and al, 0x80
00AC5ED3  B9 01 00 00 00                  mov ecx, 1
00AC5ED8  0A C3                           or al, bl
00AC5EDA  88 05 3F 15 3A 00               mov byte ptr [rip + 0x3a153f], al
00AC5EE0  E8 BB C8 9E FF                  call 0x1404b27a0
00AC5EE5  48 8D 0D F4 92 44 00            lea rcx, [rip + 0x4492f4]
00AC5EEC  E8 CB 9C 81 FF                  call 0x1402dfbbc
00AC5EF1  48 83 C4 20                     add rsp, 0x20
00AC5EF5  5B                              pop rbx
00AC5EF6  C3                              ret
00AC5EF7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopRecordBatteryPercentage(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 4494109, a2, a3, a4);
    v_rbx = (unsigned __int8)(((unsigned int)(a1)) & (127));
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3806545)) & (128));
    result = (unsigned __int8)((result) | ((unsigned __int8)(v_rbx)));
    *(unsigned __int8 *)(v_rip + 3806527) = (unsigned __int8)(result);
    result = PopBsdHandleRequest(1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4494068, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopRecordBatteryPercentage(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = PopAcquireRwLockExclusive(v_rip + 4494109, a2, a3, a4);
    local_rbx = (uint8_t)(((uint32_t)(Arg1)) & (127));
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x3A1551)) & (128));
    result = (uint8_t)((result) | ((uint8_t)(local_rbx)));
    *(uint8_t *)(v_rip + 0x3A153F) = (uint8_t)(result);
    result = PopBsdHandleRequest(1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4494068, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC5EB4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC5EB4[BB_00AC5EB4]
  bb_00AC5EF7[BB_00AC5EF7]
```
