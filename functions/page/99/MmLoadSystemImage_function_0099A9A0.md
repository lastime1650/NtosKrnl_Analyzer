# MmLoadSystemImage

- RVA: `0x0099A9A0`–`0x0099A9DB` (길이 `59` bytes)
- VA: `0x000000014099A9A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E10`
- 디코드: `15`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0099A9C9` → [MmLoadSystemImageEx](MmLoadSystemImageEx_function_00999B8C.md) (function, `0x00999B8C`)

### Direct callers
- [IoLoadCrashDumpDriver](../../text/59/IoLoadCrashDumpDriver_function_00592AD0.md) at `0x00592B2F`
- [PnprLoadPluginDriver](../73/PnprLoadPluginDriver_function_00739FC4.md) at `0x0073A028`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF53BF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0099A9A0  48 83 EC 48                     sub rsp, 0x48
0099A9A4  41 F7 C1 FC FF FF 7F            test r9d, 0x7ffffffc
0099A9AB  75 27                           jne 0x14099a9d4
0099A9AD  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
0099A9B2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0099A9B7  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
0099A9BC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0099A9C1  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
0099A9C6  45 33 C9                        xor r9d, r9d
0099A9C9  E8 BE F1 FF FF                  call 0x140999b8c
0099A9CE  48 83 C4 48                     add rsp, 0x48
0099A9D2  C3                              ret
0099A9D3  CC                              int3
0099A9D4  B8 F2 00 00 C0                  mov eax, 0xc00000f2
0099A9D9  EB F3                           jmp 0x14099a9ce
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MmLoadSystemImage(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if (((a4) & (0x7FFFFFFCULL)) != 0) goto loc_0099A9D4;
    v_stack_m18 = a6;
    v_stack_m20 = a5;
    v_stack_m28 = a4;
    a4 = 0;
    result = MmLoadSystemImageEx(a1, a2, a3, a4);
loc_0099A9CE:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0099A9D4:
    goto loc_0099A9CE;
}
```

## 5. (Beta) C Style

```c
int64_t MmLoadSystemImage(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if (((Arg4) & (0x7FFFFFFCULL)) != 0) goto loc_0099A9D4;
    v_stack_m18 = Arg6;
    v_stack_m20 = Arg5;
    v_stack_m28 = Arg4;
    Arg4 = 0;
    result = MmLoadSystemImageEx(Arg1, Arg2, Arg3, Arg4);
loc_0099A9CE:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0099A9D4:
    goto loc_0099A9CE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099A9A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099A9A0[BB_0099A9A0]
  bb_0099A9AD[BB_0099A9AD]
  bb_0099A9CE[BB_0099A9CE]
  bb_0099A9D3[BB_0099A9D3]
  bb_0099A9D4[BB_0099A9D4]
  bb_0099A9A0 -->|branch| bb_0099A9D4
  bb_0099A9A0 -->|fallthrough| bb_0099A9AD
  bb_0099A9AD -->|flow| bb_0099A9CE
  bb_0099A9D3 -->|flow| bb_0099A9D4
  bb_0099A9D4 -->|branch| bb_0099A9CE
```
