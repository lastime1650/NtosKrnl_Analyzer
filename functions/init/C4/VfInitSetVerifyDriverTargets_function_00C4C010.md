# VfInitSetVerifyDriverTargets

- RVA: `0x00C4C010`–`0x00C4C05D` (길이 `77` bytes)
- VA: `0x0000000140C4C010`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C4C044` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [ViInitSystemPhase0](ViInitSystemPhase0_function_00C4C1B0.md) at `0x00C4C384`
- [ViMakeVerifierSettings](ViMakeVerifierSettings_function_00C4CF3C.md) at `0x00C4CF94`
- [ViMakeVerifierSettings](ViMakeVerifierSettings_function_00C4CF3C.md) at `0x00C4CFBD`

### Static image references
- `0x00C4C023` → RVA `0x0100C9CE` (`INITDATA`; write)
- `0x00C4C03D` → RVA `0x0100B1D0` (`INITDATA`; read)
- `0x00C4C049` → RVA `0x00F04980` (`.data`; read/write)
- `0x00C4C050` → RVA `0x01008150` (`INITDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C4C044` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4C010  40 53                           push rbx
00C4C012  48 83 EC 20                     sub rsp, 0x20
00C4C016  41 B8 00 18 00 00               mov r8d, 0x1800
00C4C01C  41 3B D0                        cmp edx, r8d
00C4C01F  76 09                           jbe 0x140c4c02a
00C4C021  33 C0                           xor eax, eax
00C4C023  66 89 05 A4 09 3C 00            mov word ptr [rip + 0x3c09a4], ax
00C4C02A  41 3B D0                        cmp edx, r8d
00C4C02D  B8 FE 17 00 00                  mov eax, 0x17fe
00C4C032  0F 47 D0                        cmova edx, eax
00C4C035  8B DA                           mov ebx, edx
00C4C037  44 8B C2                        mov r8d, edx
00C4C03A  48 8B D1                        mov rdx, rcx
00C4C03D  48 8D 0D 8C F1 3B 00            lea rcx, [rip + 0x3bf18c]
00C4C044  E8 F7 A7 A7 FF                  call 0x1406c6840
00C4C049  83 25 30 89 2B 00 FE            and dword ptr [rip + 0x2b8930], 0xfffffffe
00C4C050  89 1D FA C0 3B 00               mov dword ptr [rip + 0x3bc0fa], ebx
00C4C056  48 83 C4 20                     add rsp, 0x20
00C4C05A  5B                              pop rbx
00C4C05B  C3                              ret
00C4C05C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfInitSetVerifyDriverTargets(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a2 >= = ((unsigned int)((unsigned int)(0x1800ULL)))) {
        result = 0;
        *(unsigned __int16 *)(v_rip + 3934628) = 0;
    }
    if (a2 > ((unsigned int)((unsigned int)(0x1800ULL)))) { a2 = (unsigned int)((unsigned int)(0x17FEULL)); }
    result = memcpy(v_rip + 3928460, a1, (unsigned int)(a2), a4);
    *(unsigned int *)(v_rip + 3916026) = (unsigned int)((unsigned int)(a2));
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfInitSetVerifyDriverTargets(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg2 >= = ((uint32_t)((uint32_t)(0x1800ULL)))) {
        result = 0;
        *(uint16_t *)(v_rip + 0x3C09A4) = 0;
    }
    if (Arg2 > ((uint32_t)((uint32_t)(0x1800ULL)))) { Arg2 = (uint32_t)((uint32_t)(0x17FEULL)); }
    result = memcpy(v_rip + 3928460, Arg1, (uint32_t)(Arg2), a4);
    *(uint32_t *)(v_rip + 0x3BC0FA) = (uint32_t)((uint32_t)(Arg2));
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4C010&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4C010[BB_00C4C010]
  bb_00C4C021[BB_00C4C021]
  bb_00C4C02A[BB_00C4C02A]
  bb_00C4C05C[BB_00C4C05C]
  bb_00C4C010 -->|branch| bb_00C4C02A
  bb_00C4C010 -->|fallthrough| bb_00C4C021
  bb_00C4C021 -->|flow| bb_00C4C02A
```
