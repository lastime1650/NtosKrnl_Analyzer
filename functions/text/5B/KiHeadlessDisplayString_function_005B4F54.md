# KiHeadlessDisplayString

- RVA: `0x005B4F54`–`0x005B4F80` (길이 `44` bytes)
- VA: `0x00000001405B4F54`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `14`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B4F75` → [HeadlessDispatch](../65/HeadlessDispatch_function_00655C40.md) (function, `0x00655C40`)

### Direct callers
- [KiBugCheckDebugBreak](KiBugCheckDebugBreak_function_005B3DC0.md) at `0x005B3E49`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F18`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F39`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F4A`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F5A`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F67`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F8C`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3F9D`
- [KiBugCheckProgress](KiBugCheckProgress_function_005B3E90.md) at `0x005B3FB1`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4BD6`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4BE2`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4BED`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4BF9`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C26`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C35`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C49`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C5C`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C67`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C72`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C82`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4C8D`
- [KiDisplayBlueScreen](KiDisplayBlueScreen_function_005B494C.md) at `0x005B4CA2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B4F54  48 83 EC 38                     sub rsp, 0x38
005B4F58  48 85 C9                        test rcx, rcx
005B4F5B  74 1D                           je 0x1405b4f7a
005B4F5D  48 85 D2                        test rdx, rdx
005B4F60  74 18                           je 0x1405b4f7a
005B4F62  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
005B4F68  45 33 C9                        xor r9d, r9d
005B4F6B  4C 8B C2                        mov r8, rdx
005B4F6E  48 8B D1                        mov rdx, rcx
005B4F71  41 8D 49 17                     lea ecx, [r9 + 0x17]
005B4F75  E8 C6 0C 0A 00                  call 0x140655c40
005B4F7A  48 83 C4 38                     add rsp, 0x38
005B4F7E  C3                              ret
005B4F7F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiHeadlessDisplayString(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    if (a1 == 0) goto loc_005B4F7A;
    if (a2 != 0) {
        a4 = 0;
        a3 = a2;
        a2 = a1;
        a1 = a4 + 23;
        result = HeadlessDispatch(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiHeadlessDisplayString(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    if (Arg1 == 0) goto loc_005B4F7A;
    if (Arg2 != 0) {
        Arg4 = 0;
        Arg3 = Arg2;
        Arg2 = Arg1;
        Arg1 = Arg4 + 23;
        result = HeadlessDispatch(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B4F54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B4F54[BB_005B4F54]
  bb_005B4F5D[BB_005B4F5D]
  bb_005B4F62[BB_005B4F62]
  bb_005B4F7A[BB_005B4F7A]
  bb_005B4F7F[BB_005B4F7F]
  bb_005B4F54 -->|branch| bb_005B4F7A
  bb_005B4F54 -->|fallthrough| bb_005B4F5D
  bb_005B4F5D -->|branch| bb_005B4F7A
  bb_005B4F5D -->|fallthrough| bb_005B4F62
  bb_005B4F62 -->|flow| bb_005B4F7A
```
