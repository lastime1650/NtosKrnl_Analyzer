# NormalizationList__Lock

- RVA: `0x005F1E80`–`0x005F1EDD` (길이 `93` bytes)
- VA: `0x00000001405F1E80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x005F1EA3` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x005F1EC8` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [RtlpGetNormalization](../../page/79/RtlpGetNormalization_function_0079AB58.md) at `0x0079AB7E`

### Static image references
- `0x005F1E8F` → RVA `0x00F05BD8` (`.data`; read)
- `0x005F1EA8` → RVA `0x00F05BD8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F1E80  40 53                           push rbx
005F1E82  48 83 EC 20                     sub rsp, 0x20
005F1E86  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
005F1E8F  48 8D 0D 42 3D 91 00            lea rcx, [rip + 0x913d42]
005F1E96  45 33 C0                        xor r8d, r8d
005F1E99  33 D2                           xor edx, edx
005F1E9B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
005F1EA2  90                              nop
005F1EA3  E8 88 E3 C1 FF                  call 0x140210230
005F1EA8  F0 48 0F BA 2D 26 3D 91 00 00   lock bts qword ptr [rip + 0x913d26], 0
005F1EB2  48 8B D8                        mov rbx, rax
005F1EB5  73 16                           jae 0x1405f1ecd
005F1EB7  4C 8D 05 1A 3D 91 00            lea r8, [rip + 0x913d1a]
005F1EBE  48 8B D0                        mov rdx, rax
005F1EC1  48 8D 0D 10 3D 91 00            lea rcx, [rip + 0x913d10]
005F1EC8  E8 C3 DD C1 FF                  call 0x14020fc90
005F1ECD  48 85 DB                        test rbx, rbx
005F1ED0  74 04                           je 0x1405f1ed6
005F1ED2  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
005F1ED6  48 83 C4 20                     add rsp, 0x20
005F1EDA  5B                              pop rbx
005F1EDB  C3                              ret
005F1EDC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NormalizationList__Lock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 9518402, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 9518362;
        a2 = result;
        a1 = v_rip + 9518352;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NormalizationList__Lock(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 9518402, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 9518362;
        Arg2 = result;
        Arg1 = v_rip + 9518352;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F1E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F1E80[BB_005F1E80]
  bb_005F1EB7[BB_005F1EB7]
  bb_005F1ECD[BB_005F1ECD]
  bb_005F1ED2[BB_005F1ED2]
  bb_005F1ED6[BB_005F1ED6]
  bb_005F1EDC[BB_005F1EDC]
  bb_005F1E80 -->|branch| bb_005F1ECD
  bb_005F1E80 -->|fallthrough| bb_005F1EB7
  bb_005F1EB7 -->|flow| bb_005F1ECD
  bb_005F1ECD -->|branch| bb_005F1ED6
  bb_005F1ECD -->|fallthrough| bb_005F1ED2
  bb_005F1ED2 -->|flow| bb_005F1ED6
```
