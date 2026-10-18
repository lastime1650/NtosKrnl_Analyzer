# DrvDbOpenDriverFileRegKey

- RVA: `0x00833FCC`–`0x0083400C` (길이 `64` bytes)
- VA: `0x0000000140833FCC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `16`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00834001` → [DrvDbOpenObjectRegKey](../93/DrvDbOpenObjectRegKey_function_00931060.md) (function, `0x00931060`)

### Direct callers
- [DrvDbGetDriverFileMappedProperty](DrvDbGetDriverFileMappedProperty_function_00833778.md) at `0x0083388B`
- [DrvDbGetDriverFileMappedPropertyKeys](DrvDbGetDriverFileMappedPropertyKeys_function_008338FC.md) at `0x0083399C`
- [DrvDbSetDriverFileMappedProperty](DrvDbSetDriverFileMappedProperty_function_008345E8.md) at `0x008346B0`
- [DrvDbDispatchDriverFile](../AC/DrvDbDispatchDriverFile_function_00AC8880.md) at `0x00AC8A4D`
- [DrvDbDispatchDriverFile](../AC/DrvDbDispatchDriverFile_function_00AC8880.md) at `0x00AC8A81`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00833FCC  4C 8B DC                        mov r11, rsp
00833FCF  48 83 EC 58                     sub rsp, 0x58
00833FD3  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00833FD8  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00833FE0  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00833FE4  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
00833FEC  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00833FF0  45 88 4B D0                     mov byte ptr [r11 - 0x30], r9b
00833FF4  4C 8B CA                        mov r9, rdx
00833FF7  33 D2                           xor edx, edx
00833FF9  45 89 43 C8                     mov dword ptr [r11 - 0x38], r8d
00833FFD  44 8D 42 04                     lea r8d, [rdx + 4]
00834001  E8 5A D0 0F 00                  call 0x140931060
00834006  48 83 C4 58                     add rsp, 0x58
0083400A  C3                              ret
0083400B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DrvDbOpenDriverFileRegKey(__int64 a1, __int64 a2, int a3, unsigned __int8 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (88);
    *(unsigned __int64 *)(v_rsp - 32) = a6;
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    *(unsigned __int8 *)(v_rsp - 48) = a4;
    a2 = 0;
    *(unsigned int *)(v_rsp - 56) = a3;
    result = DrvDbOpenObjectRegKey(a1, a2, a2 + 4, a2);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t DrvDbOpenDriverFileRegKey(int64_t Arg1, int64_t Arg2, int32_t Arg3, uint8_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (88);
    *(uint64_t *)(local_rsp - 0x20) = Arg6;
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    *(uint8_t *)(local_rsp - 0x30) = Arg4;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x38) = Arg3;
    result = DrvDbOpenObjectRegKey(Arg1, Arg2, Arg2 + 4, Arg2);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00833FCC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00833FCC[BB_00833FCC]
  bb_0083400B[BB_0083400B]
```
