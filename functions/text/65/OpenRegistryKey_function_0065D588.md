# OpenRegistryKey

- RVA: `0x0065D588`–`0x0065D5CA` (길이 `66` bytes)
- VA: `0x000000014065D588`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `17`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0065D5BF` → [ZwOpenKey](../6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)

### Direct callers
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D3A5`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D3D2`
- [OpenGlobalizationUserSettingsKey_ForSingleUserModel](OpenGlobalizationUserSettingsKey_ForSingleUserModel_function_0065D368.md) at `0x0065D4AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065D588  4C 8B DC                        mov r11, rsp
0065D58B  48 83 EC 58                     sub rsp, 0x58
0065D58F  33 C9                           xor ecx, ecx
0065D591  49 89 53 D8                     mov qword ptr [r11 - 0x28], rdx
0065D595  49 8B C0                        mov rax, r8
0065D598  49 89 4B D0                     mov qword ptr [r11 - 0x30], rcx
0065D59C  0F 57 C0                        xorps xmm0, xmm0
0065D59F  49 C7 43 C8 30 00 00 00         mov qword ptr [r11 - 0x38], 0x30
0065D5A7  49 C7 43 E0 40 02 00 00         mov qword ptr [r11 - 0x20], 0x240
0065D5AF  4D 8D 43 C8                     lea r8, [r11 - 0x38]
0065D5B3  8D 51 08                        lea edx, [rcx + 8]
0065D5B6  48 8B C8                        mov rcx, rax
0065D5B9  F3 0F 7F 44 24 40               movdqu xmmword ptr [rsp + 0x40], xmm0
0065D5BF  E8 4C FD 04 00                  call 0x1406ad310
0065D5C4  48 83 C4 58                     add rsp, 0x58
0065D5C8  C3                              ret
0065D5C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall OpenRegistryKey(int a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (88);
    a1 = 0;
    *(unsigned __int64 *)(v_rsp - 40) = a2;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 48;
    *(unsigned __int64 *)(v_rsp - 32) = 576;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(a3, a1 + 8, v_rsp - 56, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t OpenRegistryKey(int32_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    Arg1 = 0;
    *(uint64_t *)(local_rsp - 0x28) = Arg2;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 48;
    *(uint64_t *)(local_rsp - 0x20) = 576;
    v_stack_m18 = v_xmm0;
    result = ZwOpenKey(Arg3, Arg1 + 8, local_rsp - 56, a4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065D588&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065D588[BB_0065D588]
  bb_0065D5C9[BB_0065D5C9]
```
