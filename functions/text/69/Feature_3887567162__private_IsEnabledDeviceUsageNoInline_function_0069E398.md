# Feature_3887567162__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0069E398`–`0x0069E3CA` (길이 `50` bytes)
- VA: `0x000000014069E398`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0069E3BF` → [Feature_3887567162__private_IsEnabledFallback](Feature_3887567162__private_IsEnabledFallback_function_0069E3D0.md) (function, `0x0069E3D0`)

### Direct callers
- [BiConvertBootEnvironmentDeviceToNt](../../page/82/BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x0082408A`
- [BiConvertBootEnvironmentDeviceToNt](../../page/82/BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x008242F7`

### Static image references
- `0x0069E3A2` → RVA `0x00FC4E98` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069E398  48 83 EC 28                     sub rsp, 0x28
0069E39C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0069E3A2  8B 05 F0 6A 92 00               mov eax, dword ptr [rip + 0x926af0]
0069E3A8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0069E3AC  A8 10                           test al, 0x10
0069E3AE  74 05                           je 0x14069e3b5
0069E3B0  83 E0 01                        and eax, 1
0069E3B3  EB 0F                           jmp 0x14069e3c4
0069E3B5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0069E3BA  BA 03 00 00 00                  mov edx, 3
0069E3BF  E8 0C 00 00 00                  call 0x14069e3d0
0069E3C4  48 83 C4 28                     add rsp, 0x28
0069E3C8  C3                              ret
0069E3C9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3887567162__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9595632)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9595632)))) & (16)) == 0) goto loc_0069E3B5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9595632))) & (1));
    goto loc_0069E3C4;
loc_0069E3B5:
    result = Feature_3887567162__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069E3C4:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3887567162__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x926AF0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x926AF0)))) & (16)) == 0) goto loc_0069E3B5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x926AF0))) & (1));
    goto loc_0069E3C4;
loc_0069E3B5:
    result = Feature_3887567162__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069E3C4:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069E398&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069E398[BB_0069E398]
  bb_0069E3B0[BB_0069E3B0]
  bb_0069E3B5[BB_0069E3B5]
  bb_0069E3C4[BB_0069E3C4]
  bb_0069E3C9[BB_0069E3C9]
  bb_0069E398 -->|branch| bb_0069E3B5
  bb_0069E398 -->|fallthrough| bb_0069E3B0
  bb_0069E3B0 -->|branch| bb_0069E3C4
  bb_0069E3B5 -->|flow| bb_0069E3C4
```
