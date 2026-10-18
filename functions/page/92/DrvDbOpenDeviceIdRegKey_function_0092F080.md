# DrvDbOpenDeviceIdRegKey

- RVA: `0x0092F080`–`0x0092F0C0` (길이 `64` bytes)
- VA: `0x000000014092F080`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `16`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0092F0B5` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)

### Direct callers
- [DrvDbGetDeviceIdMappedPropertyKeys](../83/DrvDbGetDeviceIdMappedPropertyKeys_function_00833360.md) at `0x008333A7`
- [DrvDbDispatchDeviceId](DrvDbDispatchDeviceId_function_0092F490.md) at `0x0092F592`
- [DrvDbDispatchDeviceId](DrvDbDispatchDeviceId_function_0092F490.md) at `0x0092F661`
- [DrvDbGetDeviceIdMappedProperty](DrvDbGetDeviceIdMappedProperty_function_0092F690.md) at `0x0092FAA3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0092F080  4C 8B DC                        mov r11, rsp
0092F083  48 83 EC 58                     sub rsp, 0x58
0092F087  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
0092F08C  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
0092F094  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0092F098  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0092F0A0  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
0092F0A4  45 88 4B D0                     mov byte ptr [r11 - 0x30], r9b
0092F0A8  4C 8B CA                        mov r9, rdx
0092F0AB  33 D2                           xor edx, edx
0092F0AD  45 89 43 C8                     mov dword ptr [r11 - 0x38], r8d
0092F0B1  44 8D 42 05                     lea r8d, [rdx + 5]
0092F0B5  E8 A6 1F 00 00                  call 0x140931060
0092F0BA  48 83 C4 58                     add rsp, 0x58
0092F0BE  C3                              ret
0092F0BF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbOpenDeviceIdRegKey(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 32) = a6;
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    *(unsigned __int8 *)(v_rsp - 48) = a4;
    a2 = 0;
    *(unsigned int *)(v_rsp - 56) = a3;
    result = DrvDbOpenObjectRegKey(a1, a2, a2 + 5, a2);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbOpenDeviceIdRegKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x20) = Arg6;
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    *(uint8_t *)(local_rsp - 0x30) = Arg4;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x38) = Arg3;
    result = DrvDbOpenObjectRegKey(Arg1, Arg2, Arg2 + 5, Arg2);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092F080&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0092F080[BB_0092F080]
  bb_0092F0BF[BB_0092F0BF]
```
