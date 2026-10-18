# PopEtInternerLock

- RVA: `0x0098DEC0`–`0x0098DEE5` (길이 `37` bytes)
- VA: `0x000000014098DEC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0098DED3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x0098DEDE` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)

### Direct callers
- [RtlInternEntryDereference](RtlInternEntryDereference_function_0098DCB4.md) at `0x0098DD0E`

### Static image references
- `0x0098DEC4` → RVA `0x00E67A30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0098DED3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x0098DEDE` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098DEC0  48 83 EC 28                     sub rsp, 0x28
0098DEC4  48 8B 0D 65 9B 4D 00            mov rcx, qword ptr [rip + 0x4d9b65]
0098DECB  48 83 C1 28                     add rcx, 0x28
0098DECF  84 D2                           test dl, dl
0098DED1  75 0B                           jne 0x14098dede
0098DED3  E8 6C 2C AA FF                  call 0x140430b44
0098DED8  48 83 C4 28                     add rsp, 0x28
0098DEDC  C3                              ret
0098DEDD  CC                              int3
0098DEDE  E8 5D BB 94 FF                  call 0x1402d9a40
0098DEE3  EB F3                           jmp 0x14098ded8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtInternerLock(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a1 = (*(unsigned __int64 *)(v_rip + 5086053)) + (40);
    if (a2 != 0) goto loc_0098DEDE;
    result = PopAcquireRwLockExclusive(a1, a2, a3, a4);
loc_0098DED8:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0098DEDE:
    result = PopAcquireRwLockShared(a1, a2, a3, a4);
    goto loc_0098DED8;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtInternerLock(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg1 = (*(uint64_t *)(v_rip + 0x4D9B65)) + (40);
    if (Arg2 != 0) goto loc_0098DEDE;
    result = PopAcquireRwLockExclusive(Arg1, Arg2, a3, a4);
loc_0098DED8:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0098DEDE:
    result = PopAcquireRwLockShared(Arg1, Arg2, a3, a4);
    goto loc_0098DED8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098DEC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098DEC0[BB_0098DEC0]
  bb_0098DED3[BB_0098DED3]
  bb_0098DED8[BB_0098DED8]
  bb_0098DEDD[BB_0098DEDD]
  bb_0098DEDE[BB_0098DEDE]
  bb_0098DEC0 -->|branch| bb_0098DEDE
  bb_0098DEC0 -->|fallthrough| bb_0098DED3
  bb_0098DED3 -->|flow| bb_0098DED8
  bb_0098DEDD -->|flow| bb_0098DEDE
  bb_0098DEDE -->|branch| bb_0098DED8
```
