# IovInitializeIrp

- RVA: `0x00BB9418`–`0x00BB9437` (길이 `31` bytes)
- VA: `0x0000000140BB9418`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00BB942C` → [VfIoInitializeIrp](VfIoInitializeIrp_function_00BB66D4.md) (function, `0x00BB66D4`)

### Direct callers
- [IoInitializeIrpPriv](../../text/44/IoInitializeIrpPriv_function_00443710.md) at `0x0044379D`
- [IoInitializeIrp](../../text/44/IoInitializeIrp_function_00445050.md) at `0x004450DC`

### Static image references
- `0x00BB941C` → RVA `0x00FF4000` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BB9418  48 83 EC 28                     sub rsp, 0x28
00BB941C  8B 05 DE AB 43 00               mov eax, dword ptr [rip + 0x43abde]
00BB9422  85 C0                           test eax, eax
00BB9424  75 0B                           jne 0x140bb9431
00BB9426  45 33 C0                        xor r8d, r8d
00BB9429  49 8B D1                        mov rdx, r9
00BB942C  E8 A3 D2 FF FF                  call 0x140bb66d4
00BB9431  48 83 C4 28                     add rsp, 0x28
00BB9435  C3                              ret
00BB9436  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IovInitializeIrp(__int64 a1, __int64 a2, int a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = (unsigned int)(*(unsigned int *)(v_rip + 4434910));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4434910))) == 0) {
        a3 = 0;
        a2 = a4;
        result = VfIoInitializeIrp(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IovInitializeIrp(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x43ABDE));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x43ABDE))) == 0) {
        Arg3 = 0;
        Arg2 = Arg4;
        result = VfIoInitializeIrp(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BB9418&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BB9418[BB_00BB9418]
  bb_00BB9426[BB_00BB9426]
  bb_00BB9431[BB_00BB9431]
  bb_00BB9436[BB_00BB9436]
  bb_00BB9418 -->|branch| bb_00BB9431
  bb_00BB9418 -->|fallthrough| bb_00BB9426
  bb_00BB9426 -->|flow| bb_00BB9431
```
