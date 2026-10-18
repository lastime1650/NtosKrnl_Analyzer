# SSHSupportAllocatePaged

- RVA: `0x00A624FC`–`0x00A62516` (길이 `26` bytes)
- VA: `0x0000000140A624FC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A6250B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [SleepstudyHelperCreateBlockerFromGuid](../../text/3D/SleepstudyHelperCreateBlockerFromGuid_function_003D3F70.md) at `0x003D3FCD`
- [SleepstudyHelperSetBlockerFriendlyName](../../text/3D/SleepstudyHelperSetBlockerFriendlyName_function_003D4050.md) at `0x003D4089`
- [SshpWriteBlocker](../../text/49/SshpWriteBlocker_function_00496300.md) at `0x004966EF`
- [SshpCopyDataEntry](../../text/5E/SshpCopyDataEntry_function_005E1E10.md) at `0x005E1E39`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A6250B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A624FC  48 83 EC 28                     sub rsp, 0x28
00A62500  44 8B C2                        mov r8d, edx
00A62503  48 8B D1                        mov rdx, rcx
00A62506  B9 00 01 00 00                  mov ecx, 0x100
00A6250B  E8 E0 FB 11 00                  call 0x140b820f0
00A62510  48 83 C4 28                     add rsp, 0x28
00A62514  C3                              ret
00A62515  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SSHSupportAllocatePaged(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePool2(256, a1, (unsigned int)(a2), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SSHSupportAllocatePaged(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePool2(256, Arg1, (uint32_t)(Arg2), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A624FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A624FC[BB_00A624FC]
  bb_00A62515[BB_00A62515]
```
