# sub_0032E2BC

- RVA: `0x0032E2BC`–`0x0032E327` (길이 `107` bytes)
- VA: `0x000000014032E2BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076344`
- 디코드: `21`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0032E2BC` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0032E2C7` → [MiCheckProtoAccess + 0x4B](MiCheckProtoAccess_function_0032DFE0.md) (`tail-transfer`)
  - `0x0032E2E4` → [MiCheckProtoAccess + 0x4B](MiCheckProtoAccess_function_0032DFE0.md) (`tail-transfer`)
  - `0x0032E2F4` → [MiCheckProtoAccess + 0x4B](MiCheckProtoAccess_function_0032DFE0.md) (`tail-transfer`)
  - `0x0032E322` → [MiCheckProtoAccess + 0x4B](MiCheckProtoAccess_function_0032DFE0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032E2BC  48 F7 05 C1 87 C9 00 00 00 60 00  test qword ptr [rip + 0xc987c1], 0x600000
0032E2C7  0F 84 5E FD FF FF               je 0x14032e02b
0032E2CD  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0032E2D6  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
0032E2DD  80 BA 60 01 00 00 01            cmp byte ptr [rdx + 0x160], 1
0032E2E4  0F 84 41 FD FF FF               je 0x14032e02b
0032E2EA  4C 8B 82 08 05 00 00            mov r8, qword ptr [rdx + 0x508]
0032E2F1  4D 85 C0                        test r8, r8
0032E2F4  0F 84 31 FD FF FF               je 0x14032e02b
0032E2FA  49 8B CE                        mov rcx, r14
0032E2FD  48 C1 E9 03                     shr rcx, 3
0032E301  81 E1 FF 01 00 00               and ecx, 0x1ff
0032E307  49 8B 0C C8                     mov rcx, qword ptr [r8 + rcx*8]
0032E30B  F6 C1 20                        test cl, 0x20
0032E30E  74 04                           je 0x14032e314
0032E310  48 83 C8 20                     or rax, 0x20
0032E314  48 8B D0                        mov rdx, rax
0032E317  48 83 C8 42                     or rax, 0x42
0032E31B  F6 C1 42                        test cl, 0x42
0032E31E  48 0F 44 C2                     cmove rax, rdx
0032E322  E9 04 FD FF FF                  jmp 0x14032e02b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0032E2BC(void)
{
    __int64 result;

    a1 = (v_r14) >> (3);
    a1 = (unsigned int)((a1) & (511));
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1288) + a1 * 8))) & (66)) == 0) { result = result; }
}
```

## 5. (Beta) C Style

```c
void sub_0032E2BC(void)
{
    int64_t result;

    a1 = (local_r14) >> (3);
    a1 = (uint32_t)((a1) & (511));
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a1 * 8))) & (32)) != 0) {
        result = (result) | (32);
    }
    result = (result) | (66);
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x508) + a1 * 8))) & (66)) == 0) { result = result; }
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032E2BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0032E2BC[BB_0032E2BC]
  bb_0032E2CD[BB_0032E2CD]
  bb_0032E2EA[BB_0032E2EA]
  bb_0032E2FA[BB_0032E2FA]
  bb_0032E310[BB_0032E310]
  bb_0032E314[BB_0032E314]
  bb_0032E2BC -->|fallthrough| bb_0032E2CD
  bb_0032E2CD -->|fallthrough| bb_0032E2EA
  bb_0032E2EA -->|fallthrough| bb_0032E2FA
  bb_0032E2FA -->|branch| bb_0032E314
  bb_0032E2FA -->|fallthrough| bb_0032E310
  bb_0032E310 -->|flow| bb_0032E314
```
